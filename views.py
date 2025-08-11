from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForms
from django.http import HttpRequest
from .models import TarefasModel

def tarefas_home(request):
    contexto = {
        "tarefas": TarefasModel.objects.all() 
    }
    return render(request, 'tarefas/home.html', contexto)


def tarefas_adicionar(request:HttpRequest):
    if request.method == 'POST':
        formulario = TarefaForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarefas:home')
    contexto = {
        "form": TarefaForms
    }
    return render(request, 'tarefas/adicionar.html',contexto)

def tarefas_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefasModel, id=id)
    tarefa.delete()
    return redirect("tarefas:home")


def tarefas_editar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefasModel, id=id)
    if request.method == 'POST':
        formulario = TarefaForms(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    formulario = TarefaForms(instance=tarefa)
    contexto = {
        "form" : formulario
    }
    return render(request, 'tarefas/editar.html', contexto)

