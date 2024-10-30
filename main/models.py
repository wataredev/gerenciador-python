from django.db import models

# Create your models here.

class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    cor_do_cabelo = models.CharField(max_length=30)
    datar_nascimento = models.DateField()
    
    def __str__(self):
        return self.nome