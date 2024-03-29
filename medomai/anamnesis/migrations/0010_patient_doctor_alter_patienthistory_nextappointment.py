# Generated by Django 4.2.1 on 2024-03-03 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0009_patienthistory_nextappointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='nextappointment',
            field=models.DateField(null=True),
        ),
    ]
