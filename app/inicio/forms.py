from django import forms

from .models import *


class ReservaForm(forms.ModelForm):    

    vaga = forms.ChoiceField(choices=[('0', '-- Selecione -- ')] + [(vaga.id,vaga.descricao) for vaga in Vaga.objects.all()])
    cliente = forms.ChoiceField(choices=[('0', '-- Selecione -- ')] + [(cliente.id,cliente.nome) for cliente in Cliente.objects.all()])
    class Meta:
        model = Reserva
        fields = ('inicio','fim','status')

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nome','endereco','telefone','uf')