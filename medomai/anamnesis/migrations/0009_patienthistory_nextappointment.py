# Generated by Django 4.2.1 on 2024-03-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0008_patienthistory_history_alter_patienthistory_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='patienthistory',
            name='nextappointment',
            field=models.DateField(blank=True, null=True),
        ),
    ]