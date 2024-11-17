from django.forms import ModelForm
from .models import Musica


class MusicaForm(ModelForm):
    class Meta:
        model = Musica
        fields = [
            'name',
            'release_year',
            'poster_url',
        ]
        labels = {
            'name': 'Nome',
            'release_year': 'Data de Lançamento',
            'poster_url': 'URL da capa',
        }