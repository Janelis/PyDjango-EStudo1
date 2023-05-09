from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import ToDoList


#Classe responsavel por as listas de afazeres na forma de lista. Funcao ja sabe puxar uma lista de objetos da db pelo ListView importado anteriormente
class ModelListView(ListView):
    model = ToDoList
    template_name = "projetoApp/index.html"

