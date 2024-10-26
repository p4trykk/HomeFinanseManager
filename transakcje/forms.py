from django import forms
from .models import Transakcja, Kategoria

class TransakcjaForm(forms.ModelForm):
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Data transakcji"
    )
    class Meta:
        model = Transakcja
        fields = ['kategoria', 'typ', 'kwota', 'data', 'opis']
