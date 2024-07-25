from django.contrib import admin
from .models import TipoTramite, Unidad, SeguimientoTramite

class SeguimientoTramiteAdmin(admin.ModelAdmin):
    list_display = ('nroTramite', 'gestionTramite', 'unidadOrigen' ,'estado',)
    list_filter = ('nroTramite', 'gestionTramite',)
    search_fields = ('nroTramite', 'gestionTramite','unidadOrigen',)
    ordering = ('nroTramite',)

admin.site.register(TipoTramite)
admin.site.register(Unidad)
admin.site.register(SeguimientoTramite, SeguimientoTramiteAdmin)
