from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


# Create your models here.
class User(AbstractUser):
    pass

class Patient(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="patients")
    name = models.CharField(max_length=25, blank=True)
    lastname = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    phonenumber = models.CharField(max_length=15, blank=True, null=True)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return f"Patient {self.name} {self.lastname}"


class Patienthistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True, null=True, related_name="patient_history")
    date = models.DateTimeField() #date the file was created
    diagnostic =models.CharField(max_length=500, blank=True, null=True)
    history =models.CharField(max_length=500, blank=True, null=True) # Explanation of the symptoms
    prescription = models.CharField(max_length=500, blank=True, null=True)
    visit = models.CharField(max_length=30, blank=True, null=True) # Reason the patient is visiting
    nextappointment = models.DateField(null=True)

