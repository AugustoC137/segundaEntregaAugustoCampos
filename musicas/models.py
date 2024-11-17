from django.db import models
from django.conf import settings
from django.utils import timezone


class Musica(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    poster_url = models.URLField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} ({self.release_year})'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    musicas = models.ForeignKey(Musica, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'