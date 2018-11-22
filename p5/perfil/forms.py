from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, label='Username ')
    password = forms.CharField(max_length=15, label='Password ', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=15, label='Username ')
    password = forms.CharField(max_length=15, widget=forms.PasswordInput(), label='Password ')
    firstname = forms.CharField(max_length=30, label='Firstname ')
    lastname = forms.CharField(max_length=30, label='Lastname ')
    email = forms.EmailField(label='Username ')
    telnumber = forms.IntegerField(label='Telephone number ')
    birthdate = forms.DateField(label='Birth date ')