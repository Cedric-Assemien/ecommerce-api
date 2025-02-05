# Generated by Django 5.1.5 on 2025-01-28 20:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('boutique', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=254, verbose_name='Référence')),
                ('date_de_commande', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_commande_ids', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Commande',
                'verbose_name_plural': 'Commandes',
            },
        ),
        migrations.CreateModel(
            name='PanierModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=254, verbose_name='Référence')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_panier_ids', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Panier',
                'verbose_name_plural': 'Paniers',
            },
        ),
        migrations.CreateModel(
            name='ProduitCommandeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification')),
                ('commande_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produit_commande_ids', to='shop.commandemodel')),
                ('produit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commande_produit_ids', to='boutique.produitmodel', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'Produit commandé',
                'verbose_name_plural': 'Produits commandés',
            },
        ),
        migrations.CreateModel(
            name='ProduitPanierModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification')),
                ('panier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produit_panier_ids', to='shop.paniermodel')),
                ('produit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='panier_produit_ids', to='boutique.produitmodel', verbose_name='Produit')),
            ],
            options={
                'verbose_name': 'Produit du panier',
                'verbose_name_plural': 'Produits du panier',
            },
        ),
    ]
