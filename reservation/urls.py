from django.urls import path
from . import views

urlpatterns = [
    path('reserver/', views.reservation_create, name='reservation_create'),
    path('confirmation/', views.reservation_confirmation, name='reservation_confirmation'),
    path('annuler/<int:reservation_id>/', views.annuler_reservation, name='annuler_reservation'),
    path('tables/', views.liste_tables, name='list_tables'),
    path('create_table/',views.create_tables,name='table_create'),
]
