# Generated by Django 5.1.2 on 2024-10-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transakcje', '0002_alter_transakcja_opis_alter_transakcja_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategoria',
            name='typ',
            field=models.CharField(choices=[('Przychód', 'Przychód'), ('Wydatek', 'Wydatek')], default='Przychód', max_length=50),
        ),
    ]