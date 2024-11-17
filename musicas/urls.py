from django.urls import path

from . import views

app_name = 'musicas'
urlpatterns = [
    path('', views.MusicaListView.as_view(), name='index'),
    path('search/', views.search_musica, name='search'),
    path('create/', views.create_musica, name='create'),
    path('<int:musica_id>/', views.detail_musica, name='detail'),
    path('update/<int:musicas_id>/', views.update_musica, name='update'),
    path('delete/<int:musicas_id>/', views.delete_musica, name='delete'),
]