from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError('%(valor)s no es par.', params={'valor': value})