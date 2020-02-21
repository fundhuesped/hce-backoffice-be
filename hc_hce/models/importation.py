#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models, transaction
import psycopg2
import os
from datetime import date,datetime
import pandas as pd
import pytz
from rest_framework import generics, filters
from hc_common.models import DocumentType, SexType
from hc_laboratory.models import LabResult, Determinacion, DeterminacionValor, Paciente


class ImportationRegister(models.Model):
    """
    Clase que representa una fila de un archivo CSV importado
    """
    patient_id = models.IntegerField(default=0, null=True, blank=True)
    surname = models.CharField(max_length=60, null=True, blank=True)
    name = models.CharField(max_length=60, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=[('M','MASCULINO'), ('F','FEMENINO')], default='M', max_length=1, null=True, blank=True)
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

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']

    def salvar(*args, **kwargs):

        #TODO creando metodo para procesar registros

        #Obtain real ids/values from args and kwargs
        patientExternalId = args[0]['patient_id']
        determinationExternalId = args[0]['determination_id']
        determinationVersionId = args[0]['determination_version_id']
        determinationDescription = args[0]['determination_description']
        determinationCode = args[0]['determination_code']
        determinationNumber = args[0]['determination_number']
        labExternalId = args[0]['lab_id']
        labDate = args[0]['lab_Date'][:10]
        patientDocumentNumber = args[0]['documentNumber']
        patientBirthDate = args[0]['birthDate'][:10]
        patientName = args[0]['name']
        patientSurname = args[0]['surname']
        patientDocumentType = args[0]['documentType']
        patientGender = args[0]['gender']
        
        ir = ImportationRegister.objects.create(
            patient_id = patientExternalId,
            surname = patientSurname,
            name = patientName,
            birthDate = patientBirthDate,
            documentType = patientDocumentType,
            documentNumber = patientDocumentNumber,
            gender = patientGender,
            determination_id = determinationExternalId,
            determination_version_id = determinationVersionId,
            determination_description = determinationDescription,
            determination_code = determinationCode,
            determination_number = determinationNumber,
            lab_Date = labDate,
            lab_id = labExternalId,
            fully_processed = False
        )

        primera = 1
        ImportationRegister.process(ir,primera)

    def checkImportationsByPatient(patient):
        irQueryset = ImportationRegister.objects.all()
        irQueryset = irQueryset.filter(patient_id=patient.patient_id)
        irQueryset.update(processed_patient_id=patient.processed_patient_id)
        primera = 0

        for obj in irQueryset:
            ImportationRegister.process(obj, primera)

    def checkImportationsByDetermination(determination):
        irQueryset = ImportationRegister.objects.all()
        irQueryset = irQueryset.filter(determination_id=determination.determination_id)
        irQueryset.update(processed_determination_id=determination.processed_determination_id)
        primera = 0

        for obj in irQueryset:
            ImportationRegister.process(obj, primera)

    def checkImportationsByLabResult(labResult):
        irQueryset = ImportationRegister.objects.all()
        irQueryset = irQueryset.filter(lab_id=labResult.lab_id)
        irQueryset.update(processed_lab_id=labResult.processed_lab_id)
        primera = 0

        for obj in irQueryset:
            ImportationRegister.process(obj, primera)

    def process(self,primera):
        with transaction.atomic():
            patientQueryset = ImportationPatientRelationship.objects.all()
            patientQueryset = patientQueryset.filter(patient_id=self.patient_id)
            #Check if it was found
                #if true simply continue, obtain the patientInternalId
                #if not, find the patient by betiana's criteria
                    #If found, create a complete ImportationPatientRelationship & update this registry with the patientInternalId
                    #If cannot be found simply create an incomplete ImportationPatientRelationship registry & return
            if patientQueryset.count()!=0:
                foundPatient = patientQueryset.get()
                patientInternalId = foundPatient.processed_patient_id
                if patientInternalId==0 or patientInternalId == None:
                    return
            else:
                patientQueryset2 = Paciente.objects.all()
                #Filter by Betiana's criteria
                patientQueryset2 = patientQueryset2.filter(
                    models.Q(documentNumber=self.documentNumber) | 
                    models.Q(birthDate=self.birthDate) | 
                    (
                        models.Q(fatherSurname__icontains=self.surname) & 
                        (
                            models.Q(firstName__icontains=self.name) | 
                            models.Q(otherNames__icontains=self.name)
                        )
                    )
                )

                if patientQueryset2.count()!=0:
                    foundPatient = patientQueryset2.first()
                    patientInternalId = foundPatient.id
                    ImportationPatientRelationship.objects.create(
                        patient_id = self.patient_id,
                        surname = self.surname,
                        name = self.name,
                        birthDate = self.birthDate,
                        documentType = self.documentType,
                        documentNumber = self.documentNumber,
                        gender = self.gender,
                        processed_patient_id = patientInternalId,
                    )
                    #TODO update this registry
                else:
                    ImportationPatientRelationship.objects.create(
                        patient_id = self.patient_id,
                        surname = self.surname,
                        name = self.name,
                        birthDate = self.birthDate,
                        documentType = self.documentType,
                        documentNumber = self.documentNumber,
                        gender = self.gender,
                        processed_patient_id = None,
                        #DO NOT set processed_patient_id
                    )
                    return


            determinationQueryset = ImportationDeterminationRelationship.objects.all()
            determinationQueryset = determinationQueryset.filter(determination_id=self.determination_id)
            #Check if it was found
                #if true simply continue, obtain the determinationInternalId & update this registry with the determinationInternalId
                #if not,  simply create an incomplete ImportationDeterminationRelationship registry & return
            if determinationQueryset.count()!=0:
                determination = determinationQueryset.get()
                determinationInternalId = determination.processed_determination_id
                internalDetQuerySet = Determinacion.objects.all()
                internalDetQuerySet = internalDetQuerySet.filter(id=determinationInternalId)
                if internalDetQuerySet.count()!=0:
                    foundInternalDetermination = internalDetQuerySet.get()
                else:
                    return
            else:
                determinationQueryset2 = Determinacion.objects.all()
                #Filter by Betiana's criteria
                determinationQueryset2 = determinationQueryset2.filter(id=self.determination_id)
                if determinationQueryset2.count()!=0:
                    foundInternalDetermination = determinationQueryset2.first()
                    determinationInternalId = foundInternalDetermination.id
                    ImportationDeterminationRelationship.objects.create(
                        determination_id = self.determination_id,
                        determination_version_id = self.determination_version_id,
                        determination_description = self.determination_description,
                        determination_code = self.determination_code,
                        determination_number = self.determination_number,
                        processed_determination_id = determinationInternalId
                    )
                else:
                    ImportationDeterminationRelationship.objects.create(
                        determination_id = self.determination_id,
                        determination_version_id = self.determination_version_id,
                        determination_description = self.determination_description,
                        determination_code = self.determination_code,
                        determination_number = self.determination_number,
                    )
                    return

            labsQueryset = ImportationLabRelationship.objects.all()
            labsQueryset = labsQueryset.filter(lab_id=self.lab_id)
            #Check if it was found
                #if true simply continue, obtain the labInternalId
                #if not, find the lab by date
                    #If found, create a complete ImportationLabRelationship & update this registry with the labInternalId
                    #If cannot be found simply create an incomplete ImportationLabRelationship registry & return
            labInternalId = 0

            if labsQueryset.count()!=0:
                lab = labsQueryset.get()
                labInternalId = lab.processed_lab_id
                internalLabQuerySet = LabResult.objects.all()
                internalLabQuerySet = internalLabQuerySet.filter(id=labInternalId)
                if internalLabQuerySet.count()!=0:
                    foundLab = internalLabQuerySet.get()
            else:
                labsQueryset = LabResult.objects.all()
                labsQueryset = labsQueryset.filter(date__contains=self.lab_Date, paciente_id=patientInternalId)
                if labsQueryset.count()!=0:
                    foundLab = labsQueryset.first()
                    labInternalId = foundLab.id
                    ImportationLabRelationship.objects.create(
                        lab_Date = self.lab_Date,
                        lab_id = self.lab_id,
                        processed_lab_id = labInternalId,
                        paciente_id = self.processed_patient_id
                    )
                    #TODO update this registry
                else:
                    foundLab = LabResult.objects.create(
                        date=self.lab_Date,
                        paciente_id=patientInternalId
                    )
                    labInternalId = foundLab.id
                    ImportationLabRelationship.objects.create(
                        lab_Date = self.lab_Date,
                        lab_id = self.lab_id,
                        processed_lab_id = foundLab.id,
                        paciente_id = patientInternalId
                    )
            
            if labInternalId!=0 and determinationInternalId!=0:
                
                self.processed_patient_id = patientInternalId
                self.processed_determination_id = determinationInternalId
                self.processed_lab_id = labInternalId
                self.fully_processed = True
                self.save()

                labs = DeterminacionValor.objects.filter(labResult=labInternalId, determinacion=determinationInternalId)
                if labs.count()!=0:
                    foundLab = labs.get()
                    foundLab.value = self.determination_number
                    #foundLab.save()
                else:
                    DeterminacionValor.objects.create(
                        labResult=foundLab, 
                        determinacion=foundInternalDetermination,
                        value=self.determination_number,
                    )

                

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
    gender = models.CharField(choices=[('M','MASCULINO'), ('F','FEMENINO')], default='M', max_length=1, null=True, blank=True)

    created_on = models.DateField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']

    def save(self, *args, **kwargs):
        
        super(ImportationPatientRelationship, self).save(*args, **kwargs)
        print("--- Saved Patient Relationship ---")
        
        if self.processed_patient_id == 0:

            dtQueryset = DocumentType.objects.all()
            dtQueryset = dtQueryset.filter(name__iexact=self.documentType)
            if dtQueryset.count()!=0:
                dt = dtQueryset.get()
            else:
                print("Tipo de documento invalido")
                return

            if self.gender == 'F' or self.gender == 'Femenino' or self.gender == 'FEMENINO':
                gender = 'Femenino'
            else:
                gender = 'Masculino'
            
            stQueryset = SexType.objects.all()
            stQueryset = stQueryset.filter(name__iexact=gender)
            if stQueryset.count()!=0:
                st = stQueryset.get()
            else:
                print("Tipo de sexo invalido")
                return

            paciente = Paciente.objects.create(
                prospect= False,
                firstName= self.surname,
                fatherSurname= self.name,
                birthDate= self.birthDate,
                status= "Active",
                documentType = dt,
                documentNumber= self.documentNumber,
                genderAtBirth=st,
                genderOfChoice=st
            )
            #Actualizamos el dato de paciente procesado
            self.processed_patient_id = paciente.id
            self.save()

        #TODO Completar para reprocesar desde aqui los registros (llamar a metodo global/de clase)
        ImportationRegister.checkImportationsByPatient(self)
            
            

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

        if self.processed_determination_id == 0:
            print("Crea la determinacion")
            determinacion = Determinacion.objects.create(
                code=self.determination_code,
                label=self.determination_description,
                description=self.determination_description,
            )
            #Actualizamos el dato de paciente procesado
            self.processed_determination_id = determinacion.id
            self.save()

        #TODO Completar para reprocesar desde aqui los registros (llamar a metodo global/de clase)
        ImportationRegister.checkImportationsByDetermination(self)
            

class ImportationLabRelationship(models.Model):
    """
    Clase que representa la relacion entre IDs de Estudios de Laboratorio internos y los de una fila del CSV
    """
    lab_Date = models.DateField(null=True, blank=True)
    lab_id = models.IntegerField(default=0, null=True, blank=True)
    processed_lab_id = models.IntegerField(default=0, null=True, blank=True)
    paciente_id = models.IntegerField(default=0, null=True, blank=True)

    created_on = models.DateField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']

    def save(self, *args, **kwargs):
        super(ImportationLabRelationship, self).save(*args, **kwargs)
        print("--- Saved Lab Relationship ---")

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
        
        df.apply(ImportationRegister.salvar,axis=1)