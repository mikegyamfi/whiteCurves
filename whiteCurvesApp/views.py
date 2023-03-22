from django.http import HttpResponse
from django.shortcuts import render
from whiteCurvesApp import forms
from . import helper


# Create your views here.
def index(request):
    return render(request, "layouts/index.html")


def application(request):
    application_form = forms.RegistrationForm()
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            first_name = str(form.cleaned_data["first_name"])
            last_name = str(form.cleaned_data["last_name"])
            email = str(form.cleaned_data["email"])
            phone_number = str(form.cleaned_data["phone_number"])
            level_of_education = str(form.cleaned_data["level_of_education"])
            area_of_interest = str(form.cleaned_data["area_of_interest"])

            applicant_id = helper.generate_applicant_id()

            print(applicant_id)

            print(f"{first_name}\n{last_name}\n{email}\n{phone_number}\n{level_of_education}\n{area_of_interest}")
    context = {'form': application_form}
    return render(request, "layouts/registration-form.html", context=context)


def vac_hm_application(request):
    application_form = forms.VacRegistrationForm()
    if request.method == "POST":
        form = forms.VacRegistrationForm(request.POST)
        if form.is_valid():
            first_name = str(form.cleaned_data["first_name"])
            last_name = str(form.cleaned_data["last_name"])
            email = str(form.cleaned_data["email"])
            phone_number = str(form.cleaned_data["phone_number"])
            level_of_education = str(form.cleaned_data["level_of_education"])
            area_of_interest = str(form.cleaned_data["area_of_interest"])

            applicant_id = helper.generate_applicant_id()

            print(applicant_id)

            print(f"{first_name}\n{last_name}\n{email}\n{phone_number}\n{level_of_education}\n{area_of_interest}")
    context = {'form': application_form}
    return render(request, "layouts/services/vac-hm-application.html", context=context)


def honeymoon(request):
    return render(request, "layouts/services/honeymoon.html")


def chauffeur(request):
    return render(request, 'layouts/services/chauffeur.html')


def internship(request):
    return render(request, 'layouts/services/internship.html')



