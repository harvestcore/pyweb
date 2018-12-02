from django.shortcuts import render
import requests

# Create your views here.

def ipcontainer(request):
    context = {}
    # addToHistory("ipcontainer")
    return render(request, 'misc/ipcontainer.html', context)

def proyectos(request):
    context = {}
    # addToHistory("proyectos")
    return render(request, 'misc/proyectos.html', context)

def repositorios(request):
    repos = requests.get('https://api.github.com/users/harvestcore/repos').json()
    clean_repos = []

    for i in range(len(repos)):
        clean_repos.append({
            'name':repos[i]['name'],
            'description':repos[i]['description'],
            'url':repos[i]['html_url'],
            'updated_at':repos[i]['updated_at'],
            'stars':repos[i]['stargazers_count'],
            'forks':repos[i]['forks'],
            'license':repos[i]['license'],
            'language':repos[i]['language'],
            'is_fork':repos[i]['fork']
        })

    return render(request, 'misc/repositorios.html', {'repos': clean_repos})

def contacto(request):
    context = {}
    
    # addToHistory("contacto")
    return render(request, 'misc/contacto.html', context)