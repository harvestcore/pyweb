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
            form = LoginForm(request.POST)

            if form.is_valid():
                user = form.cleaned_data.get('username')
                passwd = form.cleaned_data.get('password')

                user = authenticate(username=user, password=passwd)

                if user:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/index/')
                
                    else:
                        return HttpResponse("Account disabled.")
                
                else:
                    return HttpResponse("Invalid user or password.")

        else:
            return render(request, 'main.html', {})

    
#   Vista de la actualización de perfil
#   GET: Muestra tabla con los datos del usuario
#   POST: Updatea los datos del usuario
class UpdateProfileView(TemplateView):
    template = 'modifyprofile.html'

    def get(self, request):
        form = ProfileForm()
        if context['currentuserstatus']['logged_in'] == True:
            return render(request, 'modifyprofile.html', context)
        else:
            return render(request, 'main.html', context)
        #return render(request, self.template, {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST)

        if form.is_valid():
            newUser = form.cleaned_data.get('username')
            actualUser = context['currentuserstatus']['username']
            db[newUser] = {"username":request.POST.get('username'), "password":request.POST.get('password'), "firstname":request.POST.get('firstname'), "lastname":request.POST.get('lastname'), "email":request.POST.get('email'), "telnumber":request.POST.get('telnumber'), "birthdate":request.POST.get('birthdate')}
            if actualUser != newUser:
                db.pop(actualUser)
                session['data'] = db[newUser]
                return render(request, 'logout.html', context)
            else:
                context['data'] = db[newUser]
                return render(request, 'modifyprofile', context)

    
#   Vista del logout
#   GET: Desconecta al usuario
class LogoutView(TemplateView):

    def get(self, request):
        if context['currentuserstatus']['username'] != '-' or context['currentuserstatus']['loggedIn'] == True:
            context['currentuserstatus']['username'] = '-'
            context['currentuserstatus']['logged_in'] = False
        return render(request, 'main.html', context)


#   Vista del signup.
#   GET: Muestra formulario para registrarse
#   POST: Registra al usuario
class SignupView(TemplateView):
    template = 'signup.html'
    registered = False

    def get(self, request):
        user_form = LoginForm()
        profile_form = ProfileForm()
        return render(request, self.template, {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

    def post(self, request):
        if request.method == 'POST':
            user_form = LoginForm(request.POST)
            profile_form = ProfileForm(request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit = False)
                profile.user = user
                profile.save()

                registered = True

            #else: print user_form.errors, profile_form.errors

        return HttpResponseRedirect('/index/')


#   Vista del perfil.
#   GET: Muestra datos del usuario logueado
class ProfileView(TemplateView):
    template = 'profile.html'

    def get(self, request):
        if context['currentuserstatus']['logged_in'] == True:
            return render(request, self.template, context)
        return render(request, 'main.html', context)
        




# Context // args
context = {
    'currentuser': {
        'username': '-',
        'password': '-',
        'firstname': '-',
        'lastname': '-',
        'email': '-',
        'telnumber': '-',
        'birthdate': '-',
    }, 
    'currentuserstatus': {
        'username': '-',
        'logged_in': '-'
    }
}