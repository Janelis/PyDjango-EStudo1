from django.db import models

# Create your models here.

from django.utils import timezone
from django.urls import reverse

#Funcao que retorna sete dias para frente como padrao
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


#Classes que extendem django.db.models.Model, definindo os campos dos dados
class ToDoList(models.Model):
    
    #Define a criacao de um novo titulo, que e uma sequencia de caracteres, de no maximo 100, que deve ser unica dentre as demais ToDoList.title
    title = models.CharField(max_length=100, unique=True)

    #Metodo convencional do Django para retornar a URL do item, reverse possibilita o programa a procurar a URL original definida com o nome list
    #Isso permite que possamos mudar URL e operar em cima dela sem alterar todas as suas referencias na fonte, preservando principios de DRY (dont repeat yourself)
    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    #Metodo string da classe
    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    #Titulo do item, de no maximo 100 caracteres (que agora pode ser igual a outros itens, ja que unique == True)
    title = models.CharField(max_length=100)

    #O campo pode não ser preenchido
    description = models.TextField(null=True, blank=True)
    
    #Data de criacao
    created_date = models.DateTimeField(auto_now_add=True)
    
    #Prazo
    due_date = models.DateTimeField(default=one_week_hence)
    
    #Garante relacao ONE-TO-MANY. Cada ToDoList pode ter diversos ToDoItem, porem um ToDoItem so pode pertencer a uma ToDoList
    #on_delete -> cascade permite que ao deletar a ToDoList todos os ToDoItem sejam deletados
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    #Implementa uma classe aninhada Meta, que permite o controle de parametros. Neste caso a ordenacao dos itens por prazo
    class Meta:
        ordering = ["due_date"]