from django.db import models
from accounts.models import User

class Table(models.Model):
    numero = models.IntegerField(unique=True, verbose_name="Numéro de table",blank=False)
    capacite = models.IntegerField(verbose_name="Capacité" ,blank=False)
    disponible = models.BooleanField(default=True, verbose_name="Disponible")

    def __str__(self):
        return f"Table {self.numero} ({self.capacite} places)"
    

class Reservation(models.Model):
    utilisateur = models.ForeignKey(User , on_delete=models.CASCADE)
    nom_client = models.CharField(max_length=100, verbose_name="Nom du client",blank=False)
    telephone = models.CharField(max_length=15, verbose_name="Téléphone")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Table réservée")
    date_reservation = models.DateField(verbose_name="Date de réservation")
    heure_reservation = models.TimeField(verbose_name="Heure de réservation")
    nombre_personnes = models.PositiveIntegerField(verbose_name="Nombre de personnes")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")

    def __str__(self):
        return (f"Réservation de {self.nom_client} pour la Table {self.table.numero} "
                f"le {self.date_reservation} à {self.heure_reservation}")
