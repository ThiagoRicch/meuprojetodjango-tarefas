from django import forms
from .models import TarefasModel


class TarefaForms(forms.ModelForm):
    class Meta:
        model = TarefasModel
        fields = ['nome','descricao','status_tarefas']