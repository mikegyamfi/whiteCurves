# Generated by Django 4.1.7 on 2023-03-21 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiteCurvesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacandhoneymoonregistration',
            name='num_of_weeks',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
