from django import forms

from .models import Pais

class CountryCreateForm(forms.ModelForm):
    class Meta:
        model = Pais 
        fields = ('nombre', 'fechaFundacion', 'tipoDeGobierno', 'poblacion', 'continente', 'PIB', 'moneda')
        