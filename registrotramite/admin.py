from django.contrib import admin
from .models import TipoTramite, Unidad, SeguimientoTramite, TramiteTraza

class SeguimientoTramiteAdmin(admin.ModelAdmin):
    list_display = ('nroTramite', 'gestionTramite', 'unidadOrigen' ,'estado',)
    list_filter = ('nroTramite', 'gestionTramite',)
    search_fields = ('nroTramite', 'gestionTramite','unidadOrigen',)
    ordering = ('nroTramite',)

class TramiteTrazaAdmin(admin.ModelAdmin):
    list_display = ('seguimientoTramite', 'unidadActual', 'fechaIngreso' ,'fechaSalida','estado',)
    list_filter = ('seguimientoTramite', 'fechaIngreso',)
    search_fields = ('seguimientoTramite','unidadActual',)
    ordering = ('fechaIngreso',)

admin.site.register(TipoTramite)
admin.site.register(Unidad)
admin.site.register(TramiteTraza, TramiteTrazaAdmin)
admin.site.register(SeguimientoTramite, SeguimientoTramiteAdmin)
