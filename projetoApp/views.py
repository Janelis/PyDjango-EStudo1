from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView, UpdateView
from .models import ToDoList, ToDoItem
from django.urls import reverse


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

#Classe responsavel pela criacao de novas listas 
class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context

#Classe responsavel pela criacao de novos items
class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

#Classe responsavel pela atualizacao de items dentro de listas
class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])