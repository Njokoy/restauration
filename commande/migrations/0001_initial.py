# Generated by Django 4.2.16 on 2025-03-15 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='meals/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('en_cours', 'En cours'), ('livrée', 'Livrée'), ('annulée', 'Annulée')], default='en_attente', max_length=20)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commandes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='commande.order')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commande.meal')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commande.meal')),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='commande.cart')),
            ],
        ),
    ]
