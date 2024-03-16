from django import forms
from .models import Image, Patienthistory

class uploadImage(forms.Form):
    photo = forms.ImageField()