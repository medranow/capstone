from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Patient, Patienthistory, Image, PatientImage

class PatientImageAdmin(admin.ModelAdmin):
    filter_horizontal = ("image",)


# Register your models here.
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Patienthistory)
admin.site.register(Image)
admin.site.register(PatientImage, PatientImageAdmin)
