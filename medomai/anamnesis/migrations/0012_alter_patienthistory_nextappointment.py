# Generated by Django 4.2.1 on 2024-03-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0011_alter_patienthistory_nextappointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienthistory',
            name='nextappointment',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]