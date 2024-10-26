from django.urls import path
from .views import transakcje_list, transakcja_add, transakcja_edit, transakcja_delete, raport

urlpatterns = [
    path('', transakcje_list, name='transakcje_list'),
    path('add/', transakcja_add, name='transakcja_add'),
    path('edit/<int:pk>/', transakcja_edit, name='transakcja_edit'),
    path('delete/<int:pk>/', transakcja_delete, name='transakcja_delete'),
    path('raport/', raport, name='raport'),  
]

