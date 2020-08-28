from django.db import models

# Create your models here.

UF_CHOICES = [
    ["1","AC"],
    ["2","AL"],
    ["3","AP"],
    ["4","AM"],
    ["5","BA"],
    ["6","CE"],
    ["7","DF"],
    ["8","ES"],
    ["9","GO"],
    ["10","MA"],
    ["11","MT"],
    ["12","MS"],
    ["13","MG"],
    ["14","PA"],
    ["15","PB"],
    ["16","PR"],
    ["17","PE"],
    ["18","PI"],
    ["19","RJ"],
    ["20","RN"],
    ["21","RS"],
    ["22","RO"],
    ["23","RR"],
    ["24","SC"],
    ["25","SP"],
    ["26","SE"],
    ["27","TO"]

]

STATUS_CHOICES = [
        ["T", "Livre"],
        ["F", "Ocupado"]        
    ]

QTD_VAGAS = [
    ["1", "1"],
    ["2", "2"],
    ["3", "3"],
    ["4", "4"],
    ["5", "5"],
    ["6", "6"],
    ["7", "7"],
    ["8", "8"],
    ["9", "9"],
    ["10", "10"],
    ["11", "11"],
    ["12", "12"],
    ["13", "13"],
    ["14", "14"],
    ["15", "15"],
    ["16", "16"],
    ["17", "17"],
    ["18", "18"],
    ["19", "19"],
    ["20", "20"],
    ["21", "21"],
    ["22", "22"],

]    

class Carro(models.Model):    
    modelo      = models.CharField(max_length=50, blank=True)
    placa       = models.CharField(max_length=50, blank=True)
    cor         = models.CharField(max_length=50, blank=True)
    ano         = models.CharField(max_length=50, blank=True)


class Cliente(models.Model):
    nome        = models.CharField(max_length=50, blank=True)
    endereco    = models.CharField(max_length=100, blank=True)
    telefone    = models.CharField(max_length=20, blank=True)
    uf          = models.CharField(max_length=2, choices=UF_CHOICES) 


class Vaga(models.Model):
    descricao = models.CharField(max_length=50, blank=True)
    vaga      = models.CharField(max_length=10, choices=QTD_VAGAS)


class Reserva(models.Model):
    vaga       = models.CharField(max_length=10, blank=True)
    cliente    = models.CharField(max_length=120, blank=True)
    carro      = models.CharField(max_length=80, blank=True)
    inicio     = models.CharField(max_length=10, blank=True)
    fim        = models.CharField(max_length=10, blank=True)
    status     = models.CharField(max_length=1, choices=STATUS_CHOICES) 