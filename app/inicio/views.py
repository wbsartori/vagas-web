from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.list import View

from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    reserva = Reserva.objects.values(
                                    'vaga',
                                    'cliente',
                                    'carro',                                    
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


def carros(request):

    carro = Carro.objects.values(
                                'modelo',
                                'placa',
                                'ano',
                                'cor')
    return render(request, 'list_carro.html', { 'carro': carro })    


def vagas(request):

    vagas = Vaga.objects.values(
                             'descricao',
                             'vaga')

    return render(request, 'list_vaga.html', {'vagas' : vagas })    
    

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


def post_novo_carro(request):
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = CarroForm
    return render(request, 'add_carro.html', {'form' : form})


def post_nova_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = VagaForm
    return render(request, 'add_vaga.html',{'form':form})
