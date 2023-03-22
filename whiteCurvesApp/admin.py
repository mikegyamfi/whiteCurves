from django.contrib import admin
from . import models

# Register your models here.


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["applicant_id", "first_name", "last_name", "email", "phone_number"]
    search_fields = ["applicant_id", "first_name", "last_name", "email"]


admin.site.register(models.Registration, RegistrationAdmin)
admin.site.register(models.VacAndHoneymoonRegistration)

