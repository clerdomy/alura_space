from django.urls import path
from . import views as _galeria

urlpatterns = [
    path('', _galeria.index, name='index'),
    path('imagem', _galeria.imagem, name='imagem')
]
