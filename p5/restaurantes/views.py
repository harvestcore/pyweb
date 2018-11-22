from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Restaurantes

from .forms import *

# Create your views here.


class RestBusquedaView(TemplateView):
    template = 'restaurantes.html'

    def get(self, request):
        form = SearchForm()
        return render(request, self.template, {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = SearchForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data.get('search')
                rest = Restaurantes.getListByName(name)
                return render(request, self.template, {'data':rest})

            else:
                return HttpResponseRedirect('/restaurantes/')
        else:
            return HttpResponseRedirect('/restaurantes/')



# def restaurantes(request):
#     # context['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
#     context = {
#         'current_rest' : {
#             'name': '-',
#             'id': '-',
#             'coordinates':'-',
#             'type':'-'
#         }
#     }
    
#     # addToHistory("restaurantes")
#     return render(request, 'restaurantes.html', context)

# def restaurantes_post():
#     try:
#         srchname = request.form['search_by_name']
#         rest = Restaurantes.getListByName(srchname)
#         context = {
#             'data': test
#         }

#     except:
#         context = {
#             'data': test
#         }

#     return render(request, 'restaurantes.html', context)

#     context = {
#         'current_rest' : {
#             'name': '-',
#             'id': '-',
#             'coordinates':'-',
#             'type':'-'
#         }
#     }

#     ##  Update de datos
#     try:
#         mod_rest_name = request.form['rest_name']
#         mod_rest_coord = request.form['rest_coord']
#         mod_rest_type = request.form['rest_type']
        
#         if mod_rest_name != context['current_rest']['name'] or mod_rest_coord != context['current_rest']['coordinates'] or mod_rest_type != context['current_rest']['type']:
#             Restaurantes.findAndUpdate(context['current_rest']['id'], {'name':mod_rest_name})
#             Restaurantes.findAndUpdate(context['current_rest']['id'], {'location':{'coordinates':mod_rest_coord, 'type':context['current_rest']['type']}})
#             Restaurantes.findAndUpdate(context['current_rest']['id'], {'location':{'coordinates':context['current_rest']['coordinates'], 'type':mod_rest_type}})
#             context['current_rest'] = {'name':mod_rest_name, 'id':context['current_rest']['id'], 'coordinates':mod_rest_coord, 'type':mod_rest_type}
#     except:
#         mod_rest_name = context['current_rest']['name']
#         mod_rest_coord = context['current_rest']['coordinates']
#         mod_rest_type = context['current_rest']['type']
#         context['current_rest'] = {'name':mod_rest_name, 'id':context['current_rest']['id'], 'coordinates':mod_rest_coord, 'type':mod_rest_type}

    ## Búsqueda por nombre
    
#     ## Búsqueda por ID
#     try:
#         srchid = request.form['search_by_id']
#         rest = Restaurantes.getByID(srchid)
#         context['current_rest'] = {'name':rest['name'], 'id':str(rest['_id']), 'coordinates':rest['location']['coordinates'], 'type':rest['location']['type']}
#     except:
#         srchid = None

#     ## Borrado por nombre
#     try:
#         delname = request.form['del_by_name']
#         rest = Restaurantes.delByName(delname)
#         context['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
#     except:
#         srchname = None
    
#     ## Borrado por ID
#     try:
#         delid = request.form['del_by_id']
#         rest = Restaurantes.delByID(delid)
#         context['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
#     except:
#         delid = None

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
