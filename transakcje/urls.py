
from django.urls import path
from .views import index, transakcje_list, transakcja_add, transakcja_edit, transakcja_delete, raport

urlpatterns = [
    path('', index, name='index'),  # Strona główna
    path('list/', transakcje_list, name='transakcje_list'),  # Lista transakcji
    path('add/', transakcja_add, name='transakcja_add'),  # Dodawanie transakcji
    path('edit/<int:pk>/', transakcja_edit, name='transakcja_edit'),  # Edytowanie transakcji
    path('delete/<int:pk>/', transakcja_delete, name='transakcja_delete'),  # Usuwanie transakcji
    path('raport/', raport, name='raport'),  # Raport finansowy
]
