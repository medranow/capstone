# Generated by Django 4.2.1 on 2024-03-19 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0021_rename_patient_history_patientimage_patient_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientImage',
        ),
    ]