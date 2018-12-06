from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=15, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ProfileForm(forms.Form):
    username = forms.CharField(required=False, max_length=15, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=False, max_length=15, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    firstname = forms.CharField(required=False, max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    lastname = forms.CharField(required=False, max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    email = forms.EmailField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    telnumber = forms.IntegerField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Tel. number'}))
    birthdate = forms.DateField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Birthdate'}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15, label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=15, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    firstname = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Firstname'}))
    lastname = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Lastname'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    telnumber = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Tel. number'}))
    birthdate = forms.DateField(label='', widget=forms.TextInput(attrs={'placeholder': 'Birthdate'}))