from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView

from bson.objectid import ObjectId
from .models import Restaurantes

from .forms import *

class RestBusquedaView(TemplateView):
    template = 'restaurantes.html'

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
    template = 'edit_restaurantes.html'

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
    template = 'delete_restaurantes.html'

    def get(self, request, _id = ""):
        rest = Restaurantes.getByID(_id)
        return render(request, self.template, {'current_rest': rest})

    def post(self, request, _id = ""):
        Restaurantes.delByID(_id)
        return HttpResponseRedirect('/restaurantes/')


class RestAddView(TemplateView):
    template = 'add_restaurantes.html'

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
            



#     ##  Agregar restaurante
#     try:
#         add_rest_name = request.form['add_name']
#         add_rest_coord = request.form['add_coord']
#         add_rest_type = request.form['add_type']

#         Restaurantes.add(add_rest_name, add_rest_coord, add_rest_type)
#     except:
#         add_rest_name = None
#         add_rest_coord = None
#         add_rest_type = None

#     addToHistory("restaurantes")
