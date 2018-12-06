from django.shortcuts import render

# Create your views here.

def main(request):
    # addToHistory("restaurantes")
    return render(request, 'main.html', {})
