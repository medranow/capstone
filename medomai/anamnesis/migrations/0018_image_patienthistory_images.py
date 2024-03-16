# Generated by Django 4.1.5 on 2024-03-15 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnesis', '0017_patienthistory_physicalexam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='patienthistory',
            name='images',
            field=models.ManyToManyField(to='anamnesis.image'),
        ),
    ]