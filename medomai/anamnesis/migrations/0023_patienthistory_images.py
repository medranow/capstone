# Generated by Django 4.2.1 on 2024-03-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0022_delete_patientimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='images',
            field=models.ManyToManyField(related_name='patient_histories', to='anamnesis.image'),
        ),
    ]
