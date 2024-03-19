from django import forms
from .models import Image, Patienthistory, PatientImage

class uploadImage(forms.Form):
    photo = forms.ImageField()