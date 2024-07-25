from rest_framework import serializers
from .models import SeguimientoTramite, Unidad, TramiteTraza, TipoTramite

class SeguimientoTramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoTramite
        fields = '__all__'

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'

class TipoTramiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoTramite
        fields = '__all__'

class ReporteTramites2023Serializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    tramites = SeguimientoTramiteSerializer(many=True)

class TramiteTrazaSerializer(serializers.ModelSerializer):
    class Meta:
        model: TramiteTraza
        fields = '__all__'

class ReporteTramiteTrazaSerializer(serializers.Serializer):
    tramite = SeguimientoTramiteSerializer()
    tramiteTrazas = TramiteTrazaSerializer(many=True)