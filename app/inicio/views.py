from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
    reserva = Reserva.objects.values(
                                    'vaga',
                                    'inicio',
                                    'fim',
                                    'status')
    
    return render(request, 'inicio.html', {'reserva' : reserva})