from django.shortcuts import render

# Create your views here.

def main(request):
    context = {}
    
    # addToHistory("restaurantes")
    return render(request, 'main.html', context)
