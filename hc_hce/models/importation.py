#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class Importation(models.Model):
    """
    Clase que representa la subida de un archivo CSV
    """
    csv = models.FileField()
    created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Importation, self).save(*args, **kwargs)
        print("--- File uploaded ---")
        filename = self.csv.url
        print("--- Filename: ", filename)
        # Do anything you'd like with the data in filename

