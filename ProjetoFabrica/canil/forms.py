
from django import forms
from .models import Raca, Cachorro

class RacaForm(forms.ModelForm):
    class Meta:
        model = Raca
        fields = ['nome', 'origem', 'temperamento']

class CachorroForm(forms.ModelForm):
    class Meta:
        model = Cachorro
        fields = ['nome', 'idade', 'raca', 'descricao']
