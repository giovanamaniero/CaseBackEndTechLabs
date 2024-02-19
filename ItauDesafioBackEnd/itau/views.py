import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models

def validate_cpf(value):
    """
    Validação de CPF.
    """
    cpf = re.sub(r'[^0-9]', '', value)
    if len(cpf) != 11:
        raise ValidationError(_('O CPF deve conter 11 dígitos.'), code='invalid_cpf_length')

    if cpf == cpf[::-1]:
        raise ValidationError(_('CPF inválido.'), code='invalid_cpf_pattern')
    
    

