from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from .models import db
from .forms import *



#   Vista del login
#   GET: Muestra formulario para hacer login
#   POST: Logea al usuario
class LoginView(TemplateView):
    template = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            blankform = LoginForm()
            form = LoginForm(request.POST)

            if form.is_valid():
                user = form.cleaned_data.get('username')
                passwd = form.cleaned_data.get('password')

                if user in db.keys():
                    data = db[user]
                    if data['password'] == passwd:
                        usr = {
                                'username': data['username'],
                                'email': data['email'],
                                'firstname': data['firstname'],
                                'lastname': data['lastname'],
                                'birthdate': data['birthdate'],
                                'telnumber': data['telnumber'],
                                'loggedin': True
                            }

                        request.session['current_user'] = usr

                        return HttpResponseRedirect('/')
                            
                else:
                    return render(request, self.template, {'form': blankform})

    
#   Vista de la actualización de perfil
#   GET: Muestra tabla con los datos del usuario
#   POST: Updatea los datos del usuario

class UpdateProfileView(TemplateView):
    template = 'modifyprofile.html'

    def get(self, request):
        form = ProfileForm()
        if request.session.get('current_user')['loggedin']:
            return render(request, self.template, {'form': form})
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        form = ProfileForm(request.POST)
        blankform = ProfileForm()

        if form.is_valid():
            if request.session.get('current_user')['username'] in db.keys():
                user = db[request.session.get('current_user')['username']]
                usr = {
                    'username': user['username'],
                    'password': user['password'],
                    'email': user['email'],
                    'firstname': user['firstname'],
                    'lastname': user['lastname'],
                    'birthdate': user['birthdate'],
                    'telnumber': user['telnumber']
                }

                if form.cleaned_data.get('username'):
                    usr['username'] = form.cleaned_data.get('username')

                if form.cleaned_data.get('password'):
                    usr['password'] = form.cleaned_data.get('password')

                if form.cleaned_data.get('email'):
                    usr['email'] = form.cleaned_data.get('email')

                if form.cleaned_data.get('firstname'):
                    usr['firstname'] = form.cleaned_data.get('firstname')

                if form.cleaned_data.get('lastname'):
                    usr['lastname'] = form.cleaned_data.get('lastname')

                if form.cleaned_data.get('birthdate'):
                    usr['birthdate'] = form.cleaned_data.get('birthdate')

                if form.cleaned_data.get('telnumber'):
                    usr['telnumber'] = form.cleaned_data.get('telnumber')

                usr2 = {
                        'username': usr['username'],
                        'email': usr['email'],
                        'firstname': usr['firstname'],
                        'lastname': usr['lastname'],
                        'birthdate': usr['telnumber'],
                        'telnumber': usr['birthdate'],
                        'loggedin': True
                    }

                request.session['current_user'] = usr2

                if user['username'] != usr['username']:
                    db.pop(user['username'])
                    db[usr['username']] = usr
                    return HttpResponseRedirect('/perfil/logout')
                
                else:
                    db[usr['username']] = usr
                    return render(request, self.template, {'form': blankform})

            return HttpResponseRedirect('/perfil/modifyprofile')
        
        return HttpResponseRedirect('/perfil/modifyprofile')

    
#   Vista del logout
#   GET: Desconecta al usuario
class LogoutView(TemplateView):

    def get(self, request):
        if request.session['current_user']['username'] != '' or request.session['current_user']['loggedin'] == True:
            usr = {
                    'username': '',
                    'email': '',
                    'firstname': '',
                    'lastname': '',
                    'birthdate': '',
                    'telnumber': '',
                    'loggedin': False
                }

            request.session['current_user'] = usr
        
        return HttpResponseRedirect('/')


#   Vista del signup.
#   GET: Muestra formulario para registrarse
#   POST: Registra al usuario
class SignupView(TemplateView):
    template = 'signup.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = ProfileForm(request.POST)

            if form.is_valid():
                usr = {
                    'username': form.cleaned_data.get('username'),
                    'password': form.cleaned_data.get('password'),
                    'email': form.cleaned_data.get('email'),
                    'firstname': form.cleaned_data.get('firstname'),
                    'lastname': form.cleaned_data.get('lastname'),
                    'birthdate': form.cleaned_data.get('birthdate'),
                    'telnumber': form.cleaned_data.get('telnumber')
                }

                db[usr['username']] = usr                
                return HttpResponseRedirect('/perfil/login')

        return HttpResponseRedirect('/')



#   Vista del perfil.
#   GET: Muestra datos del usuario logueado
class ProfileView(TemplateView):
    template = 'profile.html'

    def get(self, request):
        if request.session['current_user']['loggedin'] == True:
            return render(request, self.template, {})
       
        return HttpResponseRedirect('/')
