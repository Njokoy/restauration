# Generated by Django 4.2.16 on 2025-03-14 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True, verbose_name='Numéro de table')),
                ('capacite', models.IntegerField(verbose_name='Capacité')),
                ('disponible', models.BooleanField(default=True, verbose_name='Disponible')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_client', models.CharField(max_length=100, verbose_name='Nom du client')),
                ('telephone', models.CharField(max_length=15, verbose_name='Téléphone')),
                ('date_reservation', models.DateField(verbose_name='Date de réservation')),
                ('heure_reservation', models.TimeField(verbose_name='Heure de réservation')),
                ('nombre_personnes', models.PositiveIntegerField(verbose_name='Nombre de personnes')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé le')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.table', verbose_name='Table réservée')),
            ],
        ),
    ]
