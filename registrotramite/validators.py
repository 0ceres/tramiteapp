from django.core.exceptions import ValidationError
from datetime import datetime

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError('%(valor)s no es par.', params={'valor': value})
    
def validar_gestion(value):
    # GestionTramite must be the current year
    if  value > datetime.now().year :
        raise ValidationError('%(valor)s No es gestion actual.', params={'valor': value})