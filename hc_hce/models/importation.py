#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
import psycopg2
import os
from datetime import datetime
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
    determination_number = models.IntegerField(default=0, null=True, blank=True)
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

    def save(self, *args, **kwargs):
        super(ImportationRegister, self).save(*args, **kwargs)
        print("--- Register uploaded ---")
        print("--- Args", *args)
        print("--- Kwargs", *kwargs)

        #TODO creando metodo para procesar registros

        #TODO obtain real ids/values from args and kwargs
        patientExternalId = 3
        determinationExternalId = 3
        labExternalId = 3
        labDeterminationValue = 3

        patientQueryset = ImportationPatientRelationship.objects.all()
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
            patientQueryset = Paciente.objects.all()
            patientQueryset = patientQueryset.filter(patient_id=patientExternalId) #TODO Betiana's criteria
            if patientQueryset.count()!=0:
                foundPatient = patientQueryset.get()
                patientInternalId = foundPatient.id
                ImportationPatientRelationship.objects.create(
                    patient_id = patientExternalId,
                    surname = "dasd", #TODO obtain values from args
                    #name = ,
                    #birthDate = ,
                    #documentType = ,
                    #documentNumber = ,
                    processed_patient_id = patientInternalId,
                )
                #TODO update this registry
            else:
                ImportationPatientRelationship.objects.create(
                    patient_id = patientExternalId,
                    surname = "dasd", #TODO obtain values from args
                    #name = ,
                    #birthDate = ,
                    #documentType = ,
                    #documentNumber = ,
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
                determination_version_id = 3, #TODO get values from args
                determination_description = 'TODO',
                determination_code = 3,
                determination_number = 3,
            )
            return

        queryset = ImportationLabRelationship.objects.all()
        queryset = queryset.filter(lab_id=labExternalId)
        #TODO Check if it was found
            #if true simply continue, obtain the labInternalId
            #if not, find the lab by date
                #If found, create a complete ImportationLabRelationship & update this registry with the labInternalId
                #If cannot be found simply create an incomplete ImportationLabRelationship registry & return
        

        labs = DeterminacionValor.objects.filter(labResult=labInternalId, determinacion=determinationInternalId)
        if labs.count()!=0:
            #paciente = Paciente.objects.filter(pk=patient_id).get()
            foundLab = labs.get()
            foundLab.value = labDeterminationValue
        else:
            DeterminacionValor.objects.create(
                labResult=labInternalId, 
                determinacion=determinationInternalId,
                value=labDeterminationValue,
            )

        #TODO extraer metodo que sea global una vez que funcione

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
    determination_number = models.IntegerField(default=0, null=True, blank=True)
    processed_determination_id = models.IntegerField(default=0, null=True, blank=True)

    created_on = models.DateField(auto_now=True)

    class Meta:        
        """
        Metadata de la clase
        """
        ordering = ['created_on']

    def save(self, *args, **kwargs):
        super(ImportationDeterminationRelationship, self).save(*args, **kwargs)
        print("--- Saved Relationship ---")
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
        print("--- Saved Relationship ---")
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
        with open(filenameLocation, 'r') as f:
            print("--- File Opened:", f)
            #TODO continue working
            next(f) # Skip the header row.
            #TODO remember to change separator to PIPE
            cur.copy_from(f, 'hc_hce_importationregister', sep=',')
            conn.commit()

            #queryset = ImportationRegister.objects.all()
            #Make sure it was imported today
            # date_max_allowed = datetime.datetime.utcnow().replace(tzinfo=pytz.utc).replace(hour=18, minute=00)
            # date_min_allowed = datetime.datetime.utcnow().replace(tzinfo=pytz.utc).replace(hour=00, minute=00)
            # queryset = queryset.filter(created_on__gt=date_min_allowed)
            # queryset = queryset.filter(created_on__lte=date_max_allowed)


