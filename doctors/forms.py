from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from doctors.models import Doctor


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'box-input',
        'placeholder': 'Username',
        'required': True
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'box-input',
        'placeholder': 'First Name',
        'required': True
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'box-input',
        'placeholder': 'Last name',
        'required': True
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'box-input',
        'placeholder': 'Your Email',
        'required': True
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'box-input',
        'placeholder': 'Password',
        'required': True
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'box-input',
        'placeholder': 'Re-Type Password',
        'required': True
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)


class DoctorForm(ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'box-input',
        'placeholder': 'Phone Number',
        'required': True
    }))
    nid = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'box-input',
        'placeholder': 'NID Number',
        'required': True
    }))

    class Meta:
        model = Doctor
        fields = ('phone', 'nid',)