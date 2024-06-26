# Generated by Django 4.2.1 on 2024-03-19 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0023_patienthistory_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patienthistory',
            name='images',
        ),
        migrations.CreateModel(
            name='PatientImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anamnesis.image')),
                ('patient_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='anamnesis.patienthistory')),
            ],
        ),
    ]
