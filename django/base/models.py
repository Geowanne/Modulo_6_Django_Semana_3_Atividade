from django.db import models

#Tabela contato 
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    mensagem = models.CharField(max_length=3000)
    data = models.DateField(auto_now_add=True)
    lido = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.nome

#Tabela de reserva
class Reserva(models.Model):
    nome_pet = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    data_reserva = models.DateField()
    observacao = models.CharField(max_length=3000)
    