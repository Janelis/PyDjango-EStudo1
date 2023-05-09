#/PyDjangoEStudo1/projetoApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    #Se a URL estiver  vazia, "", chamar a classe ModelListView para resolver a request, mandando para a pagina "index"
    path("", views.ModelListView.as_view(), name="index"),
    
    #Se a URL corresponder a lista de numero X, executa o metodo as_view() da classe ItemListView para o objeto correspondente.
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    
    #Padroes CRUD para ToDoLists
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    
    #Padroes CRUD para ToDoItems
    path("list/<int:list_id>/item/add/", views.ItemCreate.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/", views.ItemUpdate.as_view(), name="item-update"),
]