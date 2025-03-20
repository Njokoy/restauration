from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('panier/', views.voir_panier, name='voir_panier'),
    path('ajouter-au-panier/<int:meal_id>/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('supprimer-du-panier/<int:cart_item_id>/', views.supprimer_du_panier, name='supprimer_du_panier'),
    path('vider-panier/', views.vider_panier, name='vider_panier'),
    path('passer-commande/', views.passer_commande, name='passer_commande'),
    path('historique-commandes/', views.historique_commandes, name='historique_commandes'),
    path('', views.index,name='acceuil'),
    path('dashboard/', views.dashboard, name='dashboard'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
