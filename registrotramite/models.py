from django.db import models
from .validators import validar_par

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
    nroTramite = models.DecimalField(max_digits=10, decimal_places=0, validators=[validar_par])
    gestionTramite = models.DecimalField(max_digits=4, decimal_places=0, blank=True)
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.ACTIVE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class TramiteTraza(models.Model):
    seguimientoTramite = models.ForeignKey(SeguimientoTramite, on_delete=models.CASCADE)
    unidadActual = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    fechaIngreso = models.DateTimeField(auto_now_add=True)
    fechaSalida = models.DateTimeField()
    estado = models.CharField(
        max_length=2,
        choices=Estado.choices,
        default=Estado.ACTIVE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)