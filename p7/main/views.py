from django.shortcuts import render

# Create your views here.

def main(request):
    context = {}
    
    # addToHistory("restaurantes")
    return render(request, 'main.html', context)

def contacto(request):
    context = {}
    
    # addToHistory("contacto")
    return render(request, 'contacto.html', context)