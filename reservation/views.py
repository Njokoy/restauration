from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from .forms import ReservationForm ,TableForm
from .models import Reservation, Table
from accounts.models import User
from django.contrib.auth.decorators import login_required
@login_required
def annuler_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # Rendre la table disponible à nouveau
    table = reservation.table
    table.disponible = True
    table.save()

    # Supprimer la réservation
    reservation.delete()
    
    messages.success(request, "Votre réservation a été annulée avec succès !")
    return redirect('liste_tables')  # Rediriger vers la liste des tables

@login_required
def reservation_create(request ):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        user = User.objects.get(pk=request.user.pk)
        if form.is_valid():
            reservation = form.save()
            # Optionnel : mettre à jour la disponibilité de la table
            table = reservation.table
            table.disponible = False
            table.save()
            messages.success(request, "Votre réservation a été effectuée avec succès !")
            return redirect('reservation_confirmation')
        else:
            messages.error(request, "Veuillez corriger les erreurs du formulaire.")
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {'form': form})

@login_required
def reservation_confirmation(request):
    resertions = Reservation.objects.get(utilisateur=request.user)
    return render(request, 'commande/historique.html' ,{'reservation':resertions})

@login_required
def liste_tables(request):
    tables = Table.objects.all()
    return render(request, 'reservations/liste_tables.html', {'tables': tables})

@login_required
def create_tables(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['capacite'] < 0 or form.cleaned_data['numero'] < 0:
                messages.error(request, "La capacité et le numéro doivent être des nombres positifs.")
                return redirect('table_create')
            else:
                form.save()
                messages.success(request, "La table a été créée avec succès.")
                return redirect('list_tables')
        else:
            messages.error(request, "Veuillez vérifier le formulaire et entrer des informations correctes.")
    else:
        form = TableForm()

    return render(request, 'reservations/create_table.html', {'form': form})