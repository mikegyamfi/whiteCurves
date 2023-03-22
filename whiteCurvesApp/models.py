from django.db import models


# Create your models here.
class Registration(models.Model):
    applicant_id = models.CharField(max_length=256, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, unique=True, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    address = models.CharField(max_length=256, unique=True, null=False, blank=False)
    country = models.CharField(max_length=256, unique=True, null=False, blank=False)
    phone_number = models.PositiveBigIntegerField(null=False, blank=False)
    level_of_education = models.CharField(max_length=1000, null=False, blank=False)
    area_of_interest = models.CharField(max_length=1000, null=False, blank=False)


class VacAndHoneymoonRegistration(models.Model):
    applicant_id = models.CharField(max_length=256, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=256, null=False, blank=False)
    last_name = models.CharField(max_length=256, unique=True, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone_number = models.PositiveBigIntegerField(null=False, blank=False)
    address = models.CharField(max_length=256, unique=True, null=False, blank=False)
    country = models.CharField(max_length=256, unique=True, null=False, blank=False)
    preferred_destination = models.CharField(max_length=256, unique=True, null=False, blank=False)
    num_of_weeks = models.PositiveIntegerField(unique=True, null=False, blank=False)
    start_date = models.CharField(max_length=256, unique=True, null=False, blank=False)
    end_date = models.CharField(max_length=256, unique=True, null=False, blank=False)
    num_of_persons = models.CharField(max_length=256, unique=True, null=False, blank=False)




