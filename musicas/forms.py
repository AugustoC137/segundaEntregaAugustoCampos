from django.forms import ModelForm
from .models import Musica, Comment


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
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }