from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    reserva = Reserva.objects.values(
                                    'vaga',
                                    'inicio',
                                    'fim',
                                    'status')
    
    return render(request, 'inicio.html', {'reserva' : reserva})

def clientes(request):
    cliente = Cliente.objects.values(
                                    'nome',
                                    'endereco',
                                    'telefone',
                                    'uf')
    
    return render(request, 'list_cliente.html', {'cliente' : cliente})

def post_nova_reserva(request):    
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():                        
            form.save()
            return redirect('inicio')
    else:
        form = ReservaForm
    return render(request, 'add_reserva.html', {'form':form})


def post_novo_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():                        
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm
    return render(request, 'add_cliente.html', {'form':form})