from django import forms
from .models import Image, Patienthistory, PatientImage
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField


class uploadImage(forms.Form):
    photos = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)