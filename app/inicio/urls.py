from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('nova/', post_nova_reserva, name='nova'),
    path('cliente/', post_novo_cliente, name='cliente'),
]
