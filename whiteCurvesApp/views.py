import requests
from decouple import config
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import render
from whiteCurvesApp import forms
from . import helper, models
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content


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
            country = str(form.cleaned_data["country"])
            address = str(form.cleaned_data["address"])
            phone_number = str(form.cleaned_data["phone_number"])
            level_of_education = str(form.cleaned_data["level_of_education"])
            area_of_interest = str(form.cleaned_data["area_of_interest"])
            applicant_id = helper.generate_applicant_id()
            try:
                sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
                from_email = Email('info@wcconsult.ltd')
                to_mail = To(email)
                subject = "Application Submission Successful"
                content = Content("text/html",
                                  "<p>Dear " + first_name + ", <br><br>"
                                  "Thank you for expressing an interest by filling out the form."
                                  "<br>We are very happy you have chosen White Curves Consult as the Agency you want to assist you in achieving your dreams.<br>"
                                  "Caring for clients is what we do best and we are thrilled that you want our team to help you in this process.<br>"
                                  "We will respond to you within 72hours with the needed requirements to further the process.<br><br>"
                                  "Your applicant ID is " + applicant_id + "<br><br>"
                                  "Kind Regards!"
                                  "<div style='width: 50%; height: 5px; background-color: #1B5667; margin-bottom: 10px;'></div>"
                                  "<img style='width: 50px; height: 50px;' src='https://www.wcconsult.ltd/static/images/favicon.png' alt=''>"
                                  "<h3>White Curves Consult Ltd.</h3>"
                                  "</p>  <p>Tel: <span style='text-decoration: none'>+447541994245</span> <br>Silver Royd Hill Armley, Leeds LS12 4QQ, United Kingdom<br><a style='text-decoration: none;' href='https://www.wcconsult.ltd'>www.wcconsult.ltd</a>  "
                                  "<br><br><p>Follow us on:</p> "
                                  "<a style='margin-right: 10px; text-decoration: none' href='https://instagram.com/wconsultltd?igshid=ZDdkNTZiNTM='>Instagram</a> "
                                  "<a style='margin-right: 10px; text-decoration: none' href='https://twitter.com/Wconsultltd?t=4QpFTCzbQ-bNFOwoXgoUaA&s=08'>Twitter</a> "
                                  "<a style='margin-right: 10px; text-decoration: none' href='https://www.facebook.com/prida.consults?mibextid=ZbWKwL'>Facebook</a>"
                                  "<br><br><p style='color: gray; font-size: 10px;'>This message contains confidential information and is intended only for the individual named. If you are not the named addressee you should not disseminate, distribute or copy this e-mail. Please notify the sender immediately by e-mail if you have received this e-mail by mistake and delete this e-mail from your system. E-mail transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability for any errors or omissions in the contents of this message, which arise as a result of e-mail transmission. If verification is required please request a hard-copy version.</p></p>")
                message = Mail(from_email, to_mail, subject, content)

                mail_json = message.get()

                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)

            new_applicant = models.Registration.objects.create(
                applicant_id=applicant_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address=address,
                country=country,
                level_of_education=level_of_education,
                area_of_interest=area_of_interest
            )
            new_applicant.save()

            url = f"https://sms.arkesel.com/sms/api?action=send-sms&api_key={config('ARKESEL')}&to=0271042505&from=WCCL&sms=An application has been Submitted.\nCheck it out.\nwww.wcconsult.ltd/admin"

            response = requests.request("GET", url)
            print(response.text)
    #         print(f"{first_name}\n{last_name}\n{email}\n{phone_number}\n{level_of_education}\n{area_of_interest}")
    context = {'form': application_form}
    return render(request, "layouts/registration-form.html", context=context)


def vac_hm_application(request):
    application_form = forms.VacRegistrationForm()
    if request.method == "POST":
        application_form = forms.VacRegistrationForm(request.POST)
        if application_form.is_valid():
            first_name = str(application_form.cleaned_data["first_name"])
            last_name = str(application_form.cleaned_data["last_name"])
            email = str(application_form.cleaned_data["email"])
            country = str(application_form.cleaned_data["country"])
            address = str(application_form.cleaned_data["address"])
            phone_number = str(application_form.cleaned_data["phone_number"])
            applicant_id = helper.generate_applicant_id()
            preferred_destination = str(application_form.cleaned_data["preferred_destination"])
            num_of_weeks = str(application_form.cleaned_data["number_of_weeks"])
            start_date = application_form.cleaned_data["start_date"]
            end_date = application_form.cleaned_data["end_date"]
            num_of_persons = application_form.cleaned_data["number_of_persons"]

            try:
                sg = SendGridAPIClient(config("SENDGRID_API_KEY"))
                from_email = Email('info@wcconsult.ltd')
                to_mail = To(email)
                subject = "Application Submission Successful"
                content = Content("text/html",
                                  "<p>Hello, <br><br>"
                                  "Thank you for contacting White Curves Consult Ltd."
                                  "<br>We acknowledge receipt of your email and a reply will be sent within 48 hours. <br><br>"
                                  "Your applicant ID is " + applicant_id + "<br><br>"
                                  "Kind Regards!"
                                  "<div style='width: 50%; height: 5px; background-color: #1B5667; margin-bottom: 10px;'></div>"
                                  "<img style='width: 50px; height: 50px;' src='https://www.wcconsult.ltd/static/images/favicon.png' alt=''>"
                                  "<h3>White Curves Consult Ltd.</h3>"
                                  "</p>  <p>Tel: <span style='text-decoration: none'>+447541994245</span> <br>Silver Royd Hill Armley, Leeds LS12 4QQ, United Kingdom<br><a style='text-decoration: none;' href='https://www.wcconsult.ltd'>www.wcconsult.ltd</a>  "
                                  "<br><br><p>Follow us on:</p> "
                                  "<a style='margin-right: 10px; text-decoration: none' href='https://instagram.com/wconsultltd?igshid=ZDdkNTZiNTM='>Instagram</a> "
                                  "<a style='margin-right: 10px; text-decoration: none' href='https://twitter.com/Wconsultltd?t=4QpFTCzbQ-bNFOwoXgoUaA&s=08'>Twitter</a> "
                                  "<a style='margin-right: 10px; text-decoration: none' href='https://www.facebook.com/prida.consults?mibextid=ZbWKwL'>Facebook</a>"
                                  "<br><br><p style='color: gray; font-size: 10px;'>This message contains confidential information and is intended only for the individual named. If you are not the named addressee you should not disseminate, distribute or copy this e-mail. Please notify the sender immediately by e-mail if you have received this e-mail by mistake and delete this e-mail from your system. E-mail transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability for any errors or omissions in the contents of this message, which arise as a result of e-mail transmission. If verification is required please request a hard-copy version.</p></p>")
                message = Mail(from_email, to_mail, subject, content)

                mail_json = message.get()

                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)

            new_applicant = models.VacAndHoneymoonRegistration.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address=address,
                country=country,
                preferred_destination=preferred_destination,
                start_date=start_date,
                end_date=end_date,
                num_of_weeks=num_of_weeks,
                num_of_persons=num_of_persons
            )

            new_applicant.save()
            url = f"https://sms.arkesel.com/sms/api?action=send-sms&api_key={config('ARKESEL')}&to=0271042505&from=WCCL&sms=An application has been Submitted.\nCheck it out.\nwww.wcconsult.ltd/admin"

            response = requests.request("GET", url)
            print(response.text)

    context = {'form': application_form}
    return render(request, "layouts/services/vac-hm-application.html", context=context)


def honeymoon(request):
    return render(request, "layouts/services/honeymoon.html")


def chauffeur(request):
    return render(request, 'layouts/services/chauffeur.html')


def internship(request):
    return render(request, 'layouts/services/internship.html')


def success(request):
    return render(request, "layouts/success.html")
