from django.db import models
from .validators import validar_par, validar_gestion
from django.core.exceptions import ValidationError

class Estado(models.TextChoices):
    ACTIVE = 'ac', 'Active'
    INACTIVE = 'in', 'Inactive'

class TipoTramite(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)
    observacion = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.ACTIVE,
    )
    def __str__(self):
        return self.descripcion

class Unidad(models.Model):
    descripcion = models.CharField(max_length=50, unique=True)
    telefono = models.DecimalField(max_digits=11, decimal_places=0)
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.ACTIVE,
    )
    def __str__(self):
        return self.descripcion

class SeguimientoTramite(models.Model):
    unidadOrigen = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    tipoTramite = models.ForeignKey(TipoTramite, on_delete=models.CASCADE)
    nroTramite = models.DecimalField(max_digits=10, decimal_places=0)
    gestionTramite = models.DecimalField(max_digits=4, decimal_places=0, blank=True, validators=[validar_gestion])
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.ACTIVE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def clean(self) :
        if SeguimientoTramite.objects.filter(nroTramite = self.nroTramite, gestionTramite = self.gestionTramite).exists():
            raise ValidationError('Numero de Tramite y Gestion ya existen')

class TramiteTraza(models.Model):
    seguimientoTramite = models.ForeignKey(SeguimientoTramite, on_delete=models.CASCADE)
    unidadActual = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    fechaSalida = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.ACTIVE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)