import datetime

from django import forms


class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'id': 'firstName'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'id': 'lastName'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'inputEmail4'}))
    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control', 'id': 'address'}))
    country = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control', 'id': 'country'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control', 'id': 'phone'}))
    level_of_education = forms.ChoiceField(choices=[('Diploma', 'Diploma (2 or more years)'), ('Degree', 'Degree'), ('Masters', 'Masters')], widget=forms.Select(attrs={'class': 'form-control'}))
    area_of_interest = forms.ChoiceField(choices=[('Work as a nurse in the UK', 'Work as a nurse in the UK'),
                                                  ('Work as a nurse in USA or Canada', 'Work as a nurse in USA or Canada'),
                                                  ('Work as a teacher in the UK', 'Work as a teacher in the UK'),
                                                  ('Study Abroad', 'Study Abroad'), ('Visa Consultation', 'Visa Consultation')], widget=forms.Select(attrs={'class': 'form-control'}))


class VacRegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'id': 'firstName'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'id': 'lastName'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'inputEmail4'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control', 'id': 'address'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control', 'id': 'country'}))
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control', 'id': 'phone'}))
    preferred_destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country', 'class': 'form-control', 'id': 'destination'}))
    number_of_weeks = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Number of Weeks', 'class': 'form-control', 'id': 'weeks'}))
    start_date = forms.DateField(initial=datetime.datetime.now(), widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'start-date'}))
    end_date = forms.DateField(initial=datetime.datetime.now(), widget=forms.DateInput(attrs={'class': 'form-control', 'id': 'end-date'}))
    number_of_persons = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control', 'id': 'num_of_persons'}))


