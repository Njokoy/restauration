from django import forms
from .models import Reservation ,Table
from accounts.models import User

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'nom_client',
            'telephone',
            'table',
            'date_reservation',
            'heure_reservation',
            'nombre_personnes',
        ]
        
        widgets = {
            'nom_client': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'nom'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Votre téléphone'
            }),
            'table': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'date_reservation': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'heure_reservation': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'nombre_personnes': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'min': 1,
                'placeholder': 'Nombre de personnes'
            }),
        }

class TableForm(forms.ModelForm):
    class Meta:
        model = Table 
        fields  = [
            'numero',
            'capacite',
            'disponible']
        
        widgets = {
            'numero': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'id de la table'
            }),
            'capacite': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'capacite'
            }),       
        }