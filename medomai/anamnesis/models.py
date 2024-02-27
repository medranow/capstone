from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


# Create your models here.
class User(AbstractUser):
    pass

class Patients(models.Model):
    name = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)

class Patienthistory(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, null=True, related_name="patient_history")
    date = models.DateTimeField()
    
