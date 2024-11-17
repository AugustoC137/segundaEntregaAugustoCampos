from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Musica
from django.shortcuts import render, get_object_or_404


def detail_musica(request, musica_id):
    musicas = get_object_or_404(Musica, pk=musica_id)
    context = {'musicas': musicas}
    return render(request, 'musicas/detail.html', context)

def list_musica(request):
    musicas_list = Musica.objects.all()
    context = {'musicas_list': musicas_list}
    return render(request, 'musicas/index.html', context)

def search_musica(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        musicas_list = Musica.objects.filter(name__icontains=search_term)
        context = {"musicas_list": musicas_list}
    return render(request, 'musicas/search.html', context)

def create_musica(request):
    if request.method == 'POST':
        musicas_name = request.POST['name']
        musicas_release_year = request.POST['release_year']
        musicas_poster_url = request.POST['poster_url']

        musicas = Musica(name=musicas_name,
                      release_year=musicas_release_year,
                      poster_url=musicas_poster_url)
        musicas.save()
        return HttpResponseRedirect(
            reverse('musicas:detail', args=(musicas.id, )))
    else:
        return render(request, 'musicas/create.html', {})

def update_musica(request, musicas_id):
    musicas = get_object_or_404(Musica, pk=musicas_id)

    if request.method == "POST":
        musicas.name = request.POST['name']
        musicas.release_year = request.POST['release_year']
        musicas.poster_url = request.POST['poster_url']
        musicas.save()
        return HttpResponseRedirect(
            reverse('musicas:detail', args=(musicas.id, )))

    context = {'musicas': musicas}
    return render(request, 'musicas/update.html', context)


def delete_musica(request, musicas_id):
    musicas = get_object_or_404(Musica, pk=musicas_id)

    if request.method == "POST":
        musicas.delete()
        return HttpResponseRedirect(reverse('musicas:index'))

    context = {'musicas': musicas}
    return render(request, 'musicas/delete.html', context)
