from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('nova/', post_nova_reserva, name='nova'),    
    path('cliente_novo/', post_novo_cliente, name='cliente_novo'),
    path('carro_novo/', post_novo_carro, name='carro_novo'),
    path('vaga_novo/', post_nova_vaga, name='vaga_novo'),
    path('cliente/', clientes, name='cliente'),
    path('carro/', carros, name='carro'),    
    path('vaga/', vagas, name='vaga'),
]
