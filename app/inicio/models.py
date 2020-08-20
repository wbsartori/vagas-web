from django.db import models

# Create your models here.

STATUS_CHOICES = [
        ["T", "Livre"],
        ["F", "Ocupado"]        
    ]

class Carro(models.Model):    
    modelo      = models.CharField(max_length=50, blank=True)
    placa       = models.CharField(max_length=50, blank=True)
    cor         = models.CharField(max_length=50, blank=True)
    ano         = models.CharField(max_length=50, blank=True)


class Reserva(models.Model):
    vaga    = models.CharField(max_length=10, blank=True)
    inicio  = models.CharField(max_length=10, blank=True)
    fim     = models.CharField(max_length=10, blank=True)
    status  = models.CharField(max_length=1, choices=STATUS_CHOICES) 


class Cliente(models.Model):
    nome        = models.CharField(max_length=50, blank=True)
    endereco    = models.CharField(max_length=100, blank=True)