from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from bson.objectid import ObjectId
from .models import Restaurantes, Plato

from .forms import *


class PlatoAddView(TemplateView):
    template = 'restaurantes/platos/add_plato.html'

    def get(self, request):
        form = PlatoForm()
        return render(request, self.template, {'form': form, 'error': '-'})

    def post(self, request):
        form = PlatoForm(request.POST)
        blankform = PlatoForm()
        
        if form.is_valid():
            form.save()

            return render(request, self.template, {'form': blankform, 'added': True, 'error': '-'})

        else:
            return render(request, self.template, {'form': blankform, 'added': False, 'error': 'Algunos campos son erróneos.'})


class PlatoBusquedaView(TemplateView):
    template = 'restaurantes/platos/platos.html'

    def get(self, request):
        platos = Plato.objects.all()
        return render(request, self.template, {'platos': platos})


class PlatoSeeView(TemplateView):
    template = 'restaurantes/platos/see_plato.html'

    def get(self, request, id_=""):
        plato = Plato.objects.get(id=id_)
        return render(request, self.template, {'plato': plato})

class PlatoEditView(TemplateView):
    template = 'restaurantes/platos/edit_plato.html'

    def get(self, request, id_=""):
        plato = Plato.objects.get(id=id_)
        form = PlatoForm(instance = plato)
        return render(request, self.template, {'plato': plato, 'form': form, 'error': '-'})

    def post(self, request, id_=""):
        error = '-'

        plato = Plato.objects.get(id=id_)
        form = PlatoForm(request.POST, instance = plato)

        if form.is_valid():
            form.save()

            plato = Plato.objects.get(id=id_)
            form = PlatoForm(instance = plato)

            return render(request, self.template, {'plato': plato, 'form': form, 'error': error})
        else:
            plato2 = Plato.objects.get(id=id_)
            form2 = PlatoForm(instance = plato)
            return render(request, self.template, {'plato': plato2, 'form': form2, 'added': False, 'error': form.errors})

class PlatoDeleteView(TemplateView):
    template = 'restaurantes/platos/delete_plato.html'

    def get(self, request, id_ = ""):
        plato = Plato.objects.get(id=id_)
        return render(request, self.template, {'plato': plato})

    def post(self, request, id_ = ""):
        plato = Plato.objects.get(id=id_)
        plato.delete()
        return HttpResponseRedirect('/restaurantes/platos/')

class RestBusquedaView(TemplateView):
    template = 'restaurantes/restaurantes.html'

    def get(self, request):
        form = SearchForm()
        return render(request, self.template, {'form': form, 'data': [], 'showdata': False, 'message': ''})

    def post(self, request):
        blancform = SearchForm()
        if request.method == 'POST':
            form = SearchForm(request.POST)

            if form.is_valid():
                rest = []
                if form.cleaned_data.get('name') != "":
                    name = form.cleaned_data.get('name')
                    rest = Restaurantes.getListByName(name)

                elif form.cleaned_data.get('_id') != "":
                    _id = form.cleaned_data.get('_id')
                    if type(_id) is ObjectId:
                        rest = Restaurantes.getListByID(_id)

                else:
                    return HttpResponseRedirect('/restaurantes/')

                if type(rest) is not list:
                        return render(request, self.template, {'form':blancform, 'data':[], 'showdata': False, 'message': 'No se ha encontrado ningún restaurante.'})
                
                if len(rest) == 0:
                    return render(request, self.template, {'form':blancform, 'data':[], 'showdata': False, 'message': 'No se ha encontrado ningún restaurante.'})

                return render(request, self.template, {'form':blancform, 'data':rest, 'showdata': True, 'message': ''})

            else:
                return HttpResponseRedirect('/restaurantes/')
        else:
            return HttpResponseRedirect('/restaurantes/')


class RestEditView(TemplateView):
    template = 'restaurantes/edit_restaurantes.html'

    def get(self, request, _id = ""):
        if request.method == 'GET':
            form = EditForm()
            rest = Restaurantes.getByID(str(_id))

            return render(request, self.template, {'current_rest': rest, 'form': form})

    def post(self, request, _id = ""):
        blancform = EditForm()

        if request.method == 'POST':
            form = EditForm(request.POST)

            if form.is_valid():
                rest = Restaurantes.getByID(_id)
                newname = rest['name']
                newcoord = rest['location']['coordinates']
                newtype = rest['location']['type']
                
                if form.cleaned_data.get('name') != "":
                    newname = form.cleaned_data.get('name')

                if form.cleaned_data.get('coordinates') != "":
                    newcoord = form.cleaned_data.get('coordinates')

                if form.cleaned_data.get('locationtype') != "":
                    newcoord = form.cleaned_data.get('locationtype')

                Restaurantes.findAndUpdate(_id, {'name': newname, 'location': {'coordinates': newcoord, 'type': newtype}})
                rest = Restaurantes.getByID(_id)
        
                return render(request, self.template, {'current_rest': rest, 'form': blancform})

        return HttpResponseRedirect('/restaurantes/')
        
class RestDeleteView(TemplateView):
    template = 'restaurantes/delete_restaurantes.html'

    def get(self, request, _id = ""):
        rest = Restaurantes.getByID(_id)
        return render(request, self.template, {'current_rest': rest})

    def post(self, request, _id = ""):
        Restaurantes.delByID(_id)
        return HttpResponseRedirect('/restaurantes/')


class RestAddView(TemplateView):
    template = 'restaurantes/add_restaurantes.html'

    def get(self, request):
        form = AddForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        blankform = AddForm()
        added = False

        if request.method == 'POST':
            form = AddForm(request.POST)

            if form.is_valid():
                newname = form.cleaned_data.get('name')
                newcoord = form.cleaned_data.get('coordinates')
                newtype = form.cleaned_data.get('locationtype')

                Restaurantes.add(newname, newcoord, newtype)
                rest = Restaurantes.getByName(newname)

                if rest['name'] == newname:
                    added = True

                return render(request, self.template, {'form': blankform, 'added': added, 'current_rest': rest})

            return HttpResponseRedirect('/restaurantes/')

        return HttpResponseRedirect('/restaurantes/')

        