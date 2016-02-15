from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Disease(models.Model):
    name = models.CharField(max_length=200)

class Gene(models.Model):
    name = models.CharField(max_length=200)

class DiseaseGene(models.Model):
	disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
	gene = models.ForeignKey(Gene, on_delete=models.CASCADE)

# Create your models here.
