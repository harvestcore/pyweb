from django.shortcuts import render

# Create your views here.

def ipcontainer(request):
    context = {}
    # addToHistory("ipcontainer")
    return render(request, 'ipcontainer.html', context)

def proyectos(request):
    context = {}
    # addToHistory("proyectos")
    return render(request, 'proyectos.html', context)

def repositorios(request):
    context = {}
    # addToHistory("repositorios")
    return render(request, 'repositorios.html', context)

def contacto(request):
    context = {}
    
    # addToHistory("contacto")
    return render(request, 'contacto.html', context)