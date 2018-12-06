from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from allauth.account.views import *
from allauth.socialaccount.views import *

from .models import db
from .forms import *


#### User

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

class UserSignupView(SignupView):
    template_name = 'accounts/signup.html'



#### Social

class UserConnectionsView(ConnectionsView):
    a = 0



#### Email

class UserConfirmEmailView(ConfirmEmailView):
    a = 0

class UserEmailView(EmailView):
    a = 0



#### Password

class UserPasswordSetView(PasswordSetView):
    a = 0

class UserPasswordChangeView(PasswordChangeView):
    a = 0

class UserPasswordResetView(PasswordResetView):
    a = 0