# Generated by Django 4.2.1 on 2024-04-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0025_remove_patientimage_image_patientimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientimage',
            name='image',
            field=models.ManyToManyField(related_name='images', to='anamnesis.image'),
        ),
    ]
