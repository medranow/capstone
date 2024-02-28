from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


# Create your models here.
class User(AbstractUser):
    pass

class Patients(models.Model):
    name = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)

class Patienthistory(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE, blank=True, null=True, related_name="patient_history")
    date = models.DateTimeField()
    
