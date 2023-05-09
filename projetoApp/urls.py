#/PyDjangoEStudo1/projetoApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    #Se a URL estiver  vazia, "", chamar a classe ModelListView para resolver a request, mandando para a pagina "index"
    path("", views.ModelListView.as_view(), name="index"),
    
    #se a URL corresponder a lista de numero X, executa o metodo as_view() da classe ItemListView para o objeto correspondente.
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
]