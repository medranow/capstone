# Generated by Django 4.2.1 on 2024-03-18 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0020_remove_image_file_remove_patienthistory_images_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientimage',
            old_name='patient_history',
            new_name='patient_file',
        ),
    ]
