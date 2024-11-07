from django.http import HttpResponse
from .temp_data import musica_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def detail_musica(request, musica_id):
    context = {'musica': musica_data[musica_id - 1]}
    return render(request, 'musicas/detail.html', context)

def list_musica(request):
    context = {"musica_list": musica_data}
    return render(request, 'musicas/index.html', context)

def search_musica(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "musica_list": [
                m for m in musica_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'musicas/search.html', context)

def create_musica(request):
    if request.method == 'POST':
        musica_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('musicas:detail', args=(len(musica_data), )))
    else:
        return render(request, 'musicas/create.html', {})