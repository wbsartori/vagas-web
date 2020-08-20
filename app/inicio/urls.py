from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('nova/', post_nova_reserva, name='nova'),
    path('cliente_novo/', post_novo_cliente, name='cliente_novo'),
    path('cliente/', clientes, name='cliente'),
]
