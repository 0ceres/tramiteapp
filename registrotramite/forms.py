from django import forms
from .models import SeguimientoTramite


class TramiteForm(forms.ModelForm):
    class Meta:
        model = SeguimientoTramite
        fields = '__all__'