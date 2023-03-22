# Generated by Django 4.1.7 on 2023-03-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiteCurvesApp', '0003_registration_others'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='certs',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='registration',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='registration',
            name='transcripts',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]