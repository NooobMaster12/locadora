from django import forms
from .models import Carro, Aluguel, Cliente

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'ano', 'placa']

class AluguelForm(forms.ModelForm):
    class Meta:
        model = Aluguel
        fields = ['carro', 'cliente', 'data_inicio', 'data_fim']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email']
        
