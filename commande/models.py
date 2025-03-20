from django.db import models
from accounts.models import User

# Modèle pour les repas disponibles
class Meal(models.Model):
    nom = models.CharField(max_length=255 , blank=False)
    description = models.TextField()
    prix = models.DecimalField(max_digits=6, decimal_places=2 , blank=False)
    image = models.ImageField(upload_to='meals/', blank=True, null=True)

    def __str__(self):
        return self.nom

# Modèle pour les commandes
class Order(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE , related_name='commandes',blank=False)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('en_attente', 'En attente'),
            ('en_cours', 'En cours'),
            ('livrée', 'Livrée'),
            ('annulée', 'Annulée'),
        ],
        default='en_attente'
    )

    def __str__(self):
        return f"Commande {self.id} - {self.utilisateur.username}"

# Modèle pour les repas dans une commande
class OrderItem(models.Model):
    commande = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantite} x {self.meal.nom}"

# Modèle pour gérer le panier temporaire
class Cart(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Panier de {self.utilisateur.username}"

# Modèle pour les repas dans le panier
class CartItem(models.Model):
    panier = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.meal.nom} dans le panier de {self.panier.utilisateur.username}"
