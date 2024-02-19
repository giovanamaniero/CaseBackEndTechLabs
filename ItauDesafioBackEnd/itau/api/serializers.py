from rest_framework import serializers
from itau import models

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = ['nome', 'data_nascimento','endereco','cpf','estado_civil']
