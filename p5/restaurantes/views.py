from django.shortcuts import render, HttpResponse
from .models import Restaurantes

# Create your views here.

def restaurantes(request):
    # session['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
    context = {
        'current_rest' : {
            'nombre': '-',
            'id': '-',
            'coordinates':'-',
            'type':'-'
        }
    }
    
    # addToHistory("restaurantes")
    return render(request, 'restaurantes.html', context)

def restaurantes_post():
    ##  Update de datos
    try:
        mod_rest_name = request.form['rest_name']
        mod_rest_coord = request.form['rest_coord']
        mod_rest_type = request.form['rest_type']
        
        if mod_rest_name != session['current_rest']['name'] or mod_rest_coord != session['current_rest']['coordinates'] or mod_rest_type != session['current_rest']['type']:
            Restaurantes.findAndUpdate(session['current_rest']['id'], {'name':mod_rest_name})
            Restaurantes.findAndUpdate(session['current_rest']['id'], {'location':{'coordinates':mod_rest_coord, 'type':session['current_rest']['type']}})
            Restaurantes.findAndUpdate(session['current_rest']['id'], {'location':{'coordinates':session['current_rest']['coordinates'], 'type':mod_rest_type}})
            session['current_rest'] = {'name':mod_rest_name, 'id':session['current_rest']['id'], 'coordinates':mod_rest_coord, 'type':mod_rest_type}
    except:
        mod_rest_name = session['current_rest']['name']
        mod_rest_coord = session['current_rest']['coordinates']
        mod_rest_type = session['current_rest']['type']
        session['current_rest'] = {'name':mod_rest_name, 'id':session['current_rest']['id'], 'coordinates':mod_rest_coord, 'type':mod_rest_type}

    ## Búsqueda por nombre
    try:
        srchname = request.form['search_by_name']
        rest = Restaurantes.getByName(srchname)
        session['current_rest'] = {'name':rest['name'], 'id':str(rest['_id']), 'coordinates':rest['location']['coordinates'], 'type':rest['location']['type']}
    except:
        srchname = None
    
    ## Búsqueda por ID
    try:
        srchid = request.form['search_by_id']
        rest = Restaurantes.getByID(srchid)
        session['current_rest'] = {'name':rest['name'], 'id':str(rest['_id']), 'coordinates':rest['location']['coordinates'], 'type':rest['location']['type']}
    except:
        srchid = None

    ## Borrado por nombre
    try:
        delname = request.form['del_by_name']
        rest = Restaurantes.delByName(delname)
        session['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
    except:
        srchname = None
    
    ## Borrado por ID
    try:
        delid = request.form['del_by_id']
        rest = Restaurantes.delByID(delid)
        session['current_rest'] = {'name':'-', 'id':'-', 'coordinates':'-', 'type':'-'}
    except:
        delid = None

    ##  Agregar restaurante
    try:
        add_rest_name = request.form['add_name']
        add_rest_coord = request.form['add_coord']
        add_rest_type = request.form['add_type']

        Restaurantes.add(add_rest_name, add_rest_coord, add_rest_type)
    except:
        add_rest_name = None
        add_rest_coord = None
        add_rest_type = None

    addToHistory("restaurantes")
    return render_template('restaurantes.html')
