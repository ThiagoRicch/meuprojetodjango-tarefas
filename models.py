from django.db import models

# Create your models here.

class TarefasModel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True,blank=True)
    status_tarefas = models.BooleanField(default=False)
    dt_criacao = models.DateTimeField(auto_now_add=True)