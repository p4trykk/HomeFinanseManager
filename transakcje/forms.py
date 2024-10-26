from django import forms
from .models import Transakcja, Kategoria

class TransakcjaForm(forms.ModelForm):
    class Meta:
        model = Transakcja
        fields = ['kategoria', 'typ', 'kwota', 'data', 'opis']
