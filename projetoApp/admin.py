from django.contrib import admin

# Register your models here.

from projetoApp.models import ToDoItem, ToDoList

#Importa as classes vindas das implementacoes de cada item da database criado no models.py
admin.site.register(ToDoItem)
admin.site.register(ToDoList)