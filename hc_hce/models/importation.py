#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


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


#TODO admin importation register
#TODO admin tablas intermedias

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
        super(Importation, self).save(*args, **kwargs)
        print("--- File uploaded ---")
        filename = self.csv.url
        print("--- Filename: ", filename)
        # Do anything you'd like with the data in filename

