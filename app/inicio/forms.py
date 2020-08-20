from django import forms

from .models import *


class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('vaga','inicio','fim','status')

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nome','endereco','telefone','uf')