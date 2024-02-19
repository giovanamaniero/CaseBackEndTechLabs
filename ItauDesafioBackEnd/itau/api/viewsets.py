from rest_framework import viewsets
from itau.api import serializers
from itau import models
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from itau.models import Pessoa

class PessoaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PessoaSerializer
    queryset = models.Pessoa.objects.all()


def excluir_pessoa(request, cpf):
    pessoa = get_object_or_404(Pessoa, cpf=cpf)
    if request.method == 'DELETE':
        pessoa.delete()
        return JsonResponse({'message': 'Pessoa excluída com sucesso!'})
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)