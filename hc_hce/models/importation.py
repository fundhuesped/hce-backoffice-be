#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models, transaction
import psycopg2
import os
from datetime import date,datetime
import pandas as pd
import pytz
from rest_framework import generics, filters
from hc_laboratory.models import LabResult, Determinacion, DeterminacionValor, Paciente


class ImportationRegister(models.Model):
    """
    Clase que representa una fila de un archivo CSV importado
    """
    patient_id = models.IntegerField(default=0, null=True, blank=True)
    surname = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    documentType = models.CharField(max_length=5, null=True, blank=True)
    documentNumber = models.CharField(max_length=15, null=True, blank=True)
    determination_id = models.IntegerField(default=0, null=True, blank=True)
    determination_version_id = models.IntegerField(default=0, null=True, blank=True)
    determination_description = models.CharField(max_length=150, null=True, blank=True)
    determination_code = models.CharField(max_length=10, null=True, blank=True)
    determination_number = models.CharField(max_length=150, null=True, blank=True)
    lab_Date = models.DateField(null=True, blank=True)
    lab_id = models.IntegerField(default=0, null=True, blank=True)
    processed_patient_id = models.IntegerField(default=0, null=True, blank=True)
    processed_determination_id = models.IntegerField(default=0, null=True, blank=True)
    processed_lab_id = models.IntegerField(default=0, null=True, blank=True)
    fully_processed = models.BooleanField(default=False)

    created_on = models.DateField(auto_now=True)
    gender = models.CharField(choices=[('M','MASCULINO'), ('F','FEMENINO')], default='M', max_length=1)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']

    def save(self, *args, **kwargs):

        #TODO creando metodo para procesar registros
       

        #Obtain real ids/values from args and kwargs
        patientExternalId = args[0]['patient_id']
        determinationExternalId = args[0]['determination_id']
        labExternalId = args[0]['lab_id']
        labDate = args[0]['lab_Date'][:10]
        labDeterminationValue = args[0]['determination_number']
        patientDocumentNumber = args[0]['documentNumber']
        patientBirthDate = args[0]['birthDate'][:10]
        patientName = args[0]['name']
        patientSurname = args[0]['surname']
        
        with transaction.atomic():
            patientQueryset = ImportationPatientRelationship.objects.all()
            #patientQueryset = Paciente.objects.all()
            patientQueryset = patientQueryset.filter(patient_id=patientExternalId)
            #Check if it was found
                #if true simply continue, obtain the patientInternalId
                #if not, find the patient by betiana's criteria
                    #If found, create a complete ImportationPatientRelationship & update this registry with the patientInternalId
                    #If cannot be found simply create an incomplete ImportationPatientRelationship registry & return
            if patientQueryset.count()!=0:
                foundPatient = patientQueryset.get()
                patientInternalId = foundPatient.id
            else:
                patientQueryset2 = Paciente.objects.all()
                #Filter by Betiana's criteria
                patientQueryset2 = patientQueryset2.filter(
                    models.Q(documentNumber=patientDocumentNumber) | 
                    models.Q(birthDate=patientBirthDate) | 
                    (
                        models.Q(fatherSurname__icontains=patientSurname) & 
                        (
                            models.Q(firstName__icontains=patientName) | 
                            models.Q(otherNames__icontains=patientName)
                        )
                    )
                )

                if patientQueryset2.count()!=0:
                    foundPatient = patientQueryset2.first()
                    patientInternalId = foundPatient.id
                    ImportationPatientRelationship.objects.create(
                        patient_id = patientExternalId,
                        surname = patientSurname,
                        name = patientName,
                        birthDate = patientBirthDate,
                        documentType = args[0]['documentType'],
                        documentNumber = patientDocumentNumber,
                        gender = args[0]['gender'],
                        processed_patient_id = patientInternalId,
                    )
                    #TODO update this registry
                else:
                    ImportationPatientRelationship.objects.create(
                        patient_id = patientExternalId,
                        surname = patientSurname,
                        name = patientName,
                        birthDate = patientBirthDate,
                        documentType = args[0]['documentType'],
                        documentNumber = patientDocumentNumber,
                        gender = args[0]['gender']
                        #DO NOT set processed_patient_id
                    )
                    return

            determinationQueryset = ImportationDeterminationRelationship.objects.all()
            determinationQueryset = determinationQueryset.filter(determination_id=determinationExternalId)
            #Check if it was found
                #if true simply continue, obtain the determinationInternalId & update this registry with the determinationInternalId
                #if not,  simply create an incomplete ImportationDeterminationRelationship registry & return
            if determinationQueryset.count()!=0:
                foundDetermination = determinationQueryset.get()
                determinationInternalId = foundDetermination.id
            else:
                ImportationDeterminationRelationship.objects.create(
                    determination_id = determinationExternalId,
                    determination_version_id = args[0]['determination_version_id'],
                    determination_description = args[0]['determination_description'],
                    determination_code = args[0]['determination_code'],
                    determination_number = args[0]['determination_number'],
                )
                return

            labsQueryset = ImportationLabRelationship.objects.all()
            labsQueryset = labsQueryset.filter(lab_id=labExternalId)
            #Check if it was found
                #if true simply continue, obtain the labInternalId
                #if not, find the lab by date
                    #If found, create a complete ImportationLabRelationship & update this registry with the labInternalId
                    #If cannot be found simply create an incomplete ImportationLabRelationship registry & return
            labInternalId = 0

            if labsQueryset.count()!=0:
                print("Lab FOUND")
                foundLab = labsQueryset.get()
                labInternalId = foundLab
            else:
                print("Lab ELSE FOUND")
                labsQueryset = ImportationLabRelationship.objects.all()
                labsQueryset = labsQueryset.filter(lab_Date=labDate)
                if labsQueryset.count()!=0:
                    foundLab = labsQueryset.first()
                    labInternalId = foundLab
                    ImportationLabRelationship.objects.create(
                        lab_Date = labDate,
                        lab_id = labExternalId,
                        processed_lab_id = labInternalId.id,
                    )
                    #TODO update this registry
                else:
                    print("Lab ELSE NOT FOUND")
                    ImportationLabRelationship.objects.create(
                        lab_Date = labDate,
                        lab_id = labExternalId,
                    )
            print("labInternalId")
            print(labInternalId)
            #if labInternalId!=0:
            #    labs = DeterminacionValor.objects.filter(labResult=labInternalId.id, determinacion=determinationInternalId)
            #    if labs.count()!=0:
                    #paciente = Paciente.objects.filter(pk=patient_id).get()
            #        foundLab = labs.get()
            #        foundLab.value = labDeterminationValue
            #    else:
            #        DeterminacionValor.objects.create(
            #            labResult=labInternalId, 
            #            determinacion=determinationInternalId,
            #            value=labDeterminationValue,
            #        )

            #TODO extraer metodo que sea global una vez que funcione
        #super(ImportationRegister, self).save(*args, **kwargs)

class ImportationPatientRelationship(models.Model):
    """
    Clase que representa la relacion entre IDs de pacientes internos y los de una fila del CSV
    """
    patient_id = models.IntegerField(default=0, null=True, blank=True)
    surname = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    documentType = models.CharField(max_length=5, null=True, blank=True)
    documentNumber = models.CharField(max_length=15, null=True, blank=True)
    processed_patient_id = models.IntegerField(default=0, null=True, blank=True)
    gender = models.CharField(choices=[('M','MASCULINO'), ('F','FEMENINO')], default='M', max_length=1)

    created_on = models.DateField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']

    def save(self, *args, **kwargs):
        super(ImportationPatientRelationship, self).save(*args, **kwargs)
        print("--- Saved Relationship ---")
        #TODO Completar para reprocesar desde aqui los registros (llamar a metodo global/de clase)

class ImportationDeterminationRelationship(models.Model):
    """
    Clase que representa la relacion entre IDs de Determinaciones internos y los de una fila del CSV
    """
    determination_id = models.IntegerField(default=0, null=True, blank=True)
    determination_version_id = models.IntegerField(default=0, null=True, blank=True)
    determination_description = models.CharField(max_length=150, null=True, blank=True)
    determination_code = models.CharField(max_length=10, null=True, blank=True)
    determination_number = models.CharField(max_length=150, null=True, blank=True)
    processed_determination_id = models.IntegerField(default=0, null=True, blank=True)

    created_on = models.DateField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']

    def save(self, *args, **kwargs):
        super(ImportationDeterminationRelationship, self).save(*args, **kwargs)
        print("--- Saved Det Relationship ---")
        #TODO Completar para reprocesar desde aqui los registros (llamar a metodo global/de clase)

class ImportationLabRelationship(models.Model):
    """
    Clase que representa la relacion entre IDs de Estudios de Laboratorio internos y los de una fila del CSV
    """
    lab_Date = models.DateField(null=True, blank=True)
    lab_id = models.IntegerField(default=0, null=True, blank=True)
    processed_lab_id = models.IntegerField(default=0, null=True, blank=True)

    created_on = models.DateField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']

    def save(self, *args, **kwargs):
        super(ImportationLabRelationship, self).save(*args, **kwargs)
        print("--- Saved Lab Relationship ---")
        #TODO Completar para reprocesar desde aqui los registros (llamar a metodo global/de clase)

class Importation(models.Model):
    """
    Clase que representa la subida de un archivo CSV
    """
    csv = models.FileField()
    created = models.DateTimeField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created']

    def save(self, *args, **kwargs):
        DB_NAME = os.getenv('DB_NAME','hce')
        DB_USER = os.getenv('DB_USER','postgres')
        DB_PASSWORD = os.getenv('DB_PASSWORD','1234')
        DB_HOST = os.getenv('DB_HOST','localhost')
        DB_PORT = os.getenv('DB_PORT','32768')

        super(Importation, self).save(*args, **kwargs)
        print("--- File uploaded ---")
        filename = self.csv.url
        print("--- Filename: ", filename)
        # Do anything you'd like with the data in filename
        conn = psycopg2.connect("host="+DB_HOST+" port="+DB_PORT+" password="+DB_PASSWORD+" dbname="+DB_NAME+" user="+DB_USER)
        print("--- Connection:", conn)
        cur = conn.cursor()
        print("--- Cursor:", cur)
        #with open(DB_HOST+":"+DB_PORT+filename, 'r') as f:
        filenameLocation = filename[1:]  #Delete first / from /url/

        #Use pandas to read csv
        #Skip first row to avoid headers
        df = pd.read_csv(filenameLocation, sep='|', header=None, skiprows=1)
        
        #Set column identifications as those that are going to be saved
        df.columns = ['patient_id', 'surname', 'name', 'birthDate','gender','documentNumber','documentType',
        'determination_id','determination_version_id','determination_description','determination_code',
        'determination_number','lab_Date','lab_id'] # You can skip this line if the column names in csv file matches that in Database

        #Call save method from ImportationRegister for each row in the file
        ir = ImportationRegister()
        df.apply(ir.save,axis=1)