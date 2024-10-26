from django.db import models

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)
    typ = models.CharField(max_length=50, choices=[('Przychód', 'Przychód'), ('Wydatek', 'Wydatek')])


    def __str__(self):
        return f"{self.nazwa} ({self.typ})"

class Transakcja(models.Model):
    typ = models.CharField(max_length=10)  # 'przychód' lub 'wydatek'
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    opis = models.TextField(default="", blank=True)  # Ustawienie domyślnej wartości
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)  # Link do kategorii

    def __str__(self):
        return f"{self.typ}: {self.kwota} PLN"
