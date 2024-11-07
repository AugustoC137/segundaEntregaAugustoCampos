from django.urls import path

from . import views

app_name = 'musicas'
urlpatterns = [
    path('', views.list_musica, name='index'),
    path('search/', views.search_musica, name='search'),
    path('create/', views.create_musica, name='create'),
    path('<int:musica_id>/', views.detail_musica, name='detail'),
]