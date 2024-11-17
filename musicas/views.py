from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Musica
from .forms import MusicaForm
from django.shortcuts import render, get_object_or_404
from django.views import generic

class MusicaDetailView(generic.DetailView):
    model = Musica
    template_name = 'musicas/detail.html'
    context_object_name = 'musica'

class MusicaListView(generic.ListView):
    model = Musica
    template_name = 'musicas/index.html'
    context_object_name = 'musicas_list'

def search_musica(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        musicas_list = Musica.objects.filter(name__icontains=search_term)
        context = {"musicas_list": musicas_list}
    return render(request, 'musicas/search.html', context)

def create_musica(request):
        if request.method == 'POST':
            form = MusicaForm(request.POST)
            if form.is_valid():
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
            form = MusicaForm()
        context = {'form': form}
        return render(request, 'musicas/create.html', context)

def update_musica(request, musicas_id):
    musicas = get_object_or_404(Musica, pk=musicas_id)

    if request.method == "POST":
        form = MusicaForm(request.POST)
        if form.is_valid():
            musicas.name = request.POST['name']
            musicas.release_year = request.POST['release_year']
            musicas.poster_url = request.POST['poster_url']
            musicas.save()
            return HttpResponseRedirect(
                reverse('musicas:detail', args=(musicas.id, )))
    else:
        form = MusicaForm(
            initial={
                'name': musicas.name,
                'release_year': musicas.release_year,
                'poster_url': musicas.poster_url
            })

    context = {'musicas': musicas, 'form': form}
    return render(request, 'musicas/update.html', context)


def delete_musica(request, musicas_id):
    musicas = get_object_or_404(Musica, pk=musicas_id)

    if request.method == "POST":
        musicas.delete()
        return HttpResponseRedirect(reverse('musicas:index'))

    context = {'musicas': musicas}
    return render(request, 'musicas/delete.html', context)
