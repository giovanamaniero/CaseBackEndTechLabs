from django.db import models
from itau.views import validate_cpf

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    cpf = models.CharField(primary_key=True, max_length=11, validators=[validate_cpf])
    estado_civil = models.CharField(max_length=20)

    def __str__(self):
     return str(self.cpf)