from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import ToDoList, ToDoItem


#Classe responsavel por as listas de afazeres na forma de lista. Funcao ja sabe puxar uma lista de objetos da db pelo ListView importado anteriormente
class ModelListView(ListView):
    model = ToDoList
    template_name = "projetoApp/index.html"

#Classe responsavel por mostrar items dentro de uma lista na forma de lista.
class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    #Redefine a funcao get_queryset para usar os objetos filtrados 
    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    #Redefine a funcao get_context_data para retornar os objetos correspondentes ao filtro dentro de .get()
    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context