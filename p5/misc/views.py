from django.shortcuts import render

# Create your views here.

def ipcontainer(request):
    context = {}
    # addToHistory("ipcontainer")
    return render(request, 'ipcontainer.html', context)

def proyectos(request):
    context = {}
    # addToHistory("proyectos")
    return render_template(request, 'proyectos.html', context)

def repositorios(request):
    context = {}
    # addToHistory("repositorios")
    return render_template(request, 'repositorios.html', context)