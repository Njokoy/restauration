from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Meal, Cart, CartItem, Order, OrderItem

# 1️⃣ Afficher le menu des repas
def menu(request):
    meals = Meal.objects.all()
    return render(request, 'commande/menu.html', {'meals': meals})

# 2️⃣ Voir le panier
@login_required
def voir_panier(request):
    cart, created = Cart.objects.get_or_create(utilisateur=request.user)
    items = CartItem.objects.filter(panier=cart)
    total = sum(item.meal.prix * item.quantite for item in items)
    
    return render(request, 'commande/panier.html', {'items': items, 'total': total})

# 3️⃣ Ajouter un repas au panier
@login_required
def ajouter_au_panier(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    cart, created = Cart.objects.get_or_create(utilisateur=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(panier=cart, meal=meal)
    if not created:
        cart_item.quantite += 1
        cart_item.save()
    
    messages.success(request, f"{meal.nom} a été ajouté au panier.")
    return redirect('menu')

# 4️⃣ Supprimer un repas du panier
@login_required
def supprimer_du_panier(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, panier__utilisateur=request.user)
    cart_item.delete()
    
    messages.success(request, "Article supprimé du panier.")
    return redirect('voir_panier')

# 5️⃣ Vider le panier
@login_required
def vider_panier(request):
    cart, created = Cart.objects.get_or_create(utilisateur=request.user)
    cart.items.all().delete()
    
    messages.success(request, "Votre panier a été vidé.")
    return redirect('voir_panier')

# 6️⃣ Passer une commande
@login_required
def passer_commande(request):
    cart = get_object_or_404(Cart, utilisateur=request.user)
    items = CartItem.objects.filter(panier=cart)

    if not items:
        messages.error(request, "Votre panier est vide.")
        return redirect('voir_panier')

    # Créer une commande
    commande = Order.objects.create(utilisateur=request.user)

    for item in items:
        OrderItem.objects.create(
            commande=commande,
            meal=item.meal,
            quantite=item.quantite
        )

    # Vider le panier après la commande
    cart.items.all().delete()

    messages.success(request, "Votre commande a été passée avec succès.")
    return redirect('historique_commandes')

# 7️⃣ Voir l’historique des commandes
@login_required
def historique_commandes(request):
    commandes = Order.objects.filter(utilisateur=request.user).order_by('-date_commande')
    return render(request, 'commande/historique.html', {'commandes': commandes})


def index(request):
    context = {"message": "Bienvenue sur mon site"}
    return render(request, "commande/index.html", context)

from django.shortcuts import render
from .models import Meal

@login_required
def dashboard(request):
    meals = Meal.objects.all()[:4]  # Récupère quelques plats du menu
    return render(request, 'commande/dashboard.html', {'meals': meals})
