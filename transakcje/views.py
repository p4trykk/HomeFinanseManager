from django.shortcuts import render, redirect, get_object_or_404
from .models import Transakcja, Kategoria
from .forms import TransakcjaForm
from django.shortcuts import render
from django.db.models import Sum

def index(request):
    return render(request, 'index.html')

def transakcje_list(request):
    kategoria_id = request.GET.get('kategoria')
    if kategoria_id:
        transakcje = Transakcja.objects.filter(kategoria__id=kategoria_id)
    else:
        transakcje = Transakcja.objects.all()
    
    kategorie = Kategoria.objects.all()
    return render(request, 'transakcje/transakcje_list.html', {
        'transakcje': transakcje,
        'kategorie': kategorie,
    })

def transakcja_add(request):
    if request.method == 'POST':
        form = TransakcjaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transakcje_list')
    else:
        form = TransakcjaForm()
    return render(request, 'transakcje/transakcja_form.html', {'form': form})

def transakcja_edit(request, pk):
    transakcja = get_object_or_404(Transakcja, pk=pk)
    if request.method == 'POST':
        form = TransakcjaForm(request.POST, instance=transakcja)
        if form.is_valid():
            form.save()
            return redirect('transakcje_list')
    else:
        form = TransakcjaForm(instance=transakcja)
    return render(request, 'transakcje/transakcja_form.html', {'form': form})

def transakcja_delete(request, pk):
    transakcja = get_object_or_404(Transakcja, pk=pk)
    if request.method == 'POST':
        transakcja.delete()
        return redirect('transakcje_list')
    return render(request, 'transakcje/transakcja_delete.html', {'transakcja': transakcja})

def raport(request):
    przychody = Transakcja.objects.filter(kategoria__typ='Przychód').aggregate(Sum('kwota'))['kwota__sum'] or 0
    wydatki = Transakcja.objects.filter(kategoria__typ='Wydatek').aggregate(Sum('kwota'))['kwota__sum'] or 0
    bilans = przychody - wydatki

    return render(request, 'transakcje/raport.html', {
        'przychody': przychody,
        'wydatki': wydatki,
        'bilans': bilans,
    })
