from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import *


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'




class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs= {'placeholder': 'Password'}))


class UserRegistrationForm(forms.ModelForm):
    CHOICES = [('Doctor','Doctor'),('Patient','Patient')]
    status = forms.CharField(label='Register As', widget=forms.RadioSelect(choices=CHOICES))
    password = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'Enter Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs= {'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if len(password) and len(confirm_password) <= 4:
            raise forms.ValidationError("Password length should be greater than 4 digits")

        if password != confirm_password:
            raise forms.ValidationError('Password Mismatch')
        return confirm_password