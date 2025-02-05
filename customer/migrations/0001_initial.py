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
            name='AdresseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=254, verbose_name='Ville')),
                ('quartier', models.CharField(max_length=254, verbose_name='Quartier')),
                ('rue', models.CharField(max_length=254, verbose_name='Rue')),
                ('longitude', models.CharField(max_length=20, verbose_name='Longitude')),
                ('latitude', models.CharField(max_length=20, verbose_name='Latitude')),
                ('indication', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_adresse_ids', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Adresse de Livraison',
                'verbose_name_plural': 'Adresses de Livraison',
            },
        ),
        migrations.CreateModel(
            name='AvisModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=254, verbose_name='Titre')),
                ('commentaire', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification')),
                ('produit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avis_produit_ids', to='boutique.produitmodel', verbose_name='Produit')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_avis_ids', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Adresse de Livraison',
                'verbose_name_plural': 'Adresses de Livraison',
            },
        ),
        migrations.CreateModel(
            name='MoyenoDePaiementModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('mobile', 'Mobile Money'), ('visa', 'Visa'), ('wave', 'Wave'), ('paypal', 'Paypal')], default='mobile', max_length=254, verbose_name='Type')),
                ('carte', models.CharField(blank=True, max_length=254, null=True, verbose_name='Numéro de la carte')),
                ('cvc', models.CharField(blank=True, max_length=254, null=True, verbose_name='CVC')),
                ('mois_expiration', models.CharField(blank=True, max_length=20, null=True, verbose_name='Mois expiration')),
                ('annee_expiration', models.CharField(blank=True, max_length=20, null=True, verbose_name='Année expiration')),
                ('adresse_paypal', models.CharField(blank=True, max_length=20, null=True, verbose_name='Adresse Paypal')),
                ('numero', models.CharField(blank=True, max_length=20, null=True, verbose_name='numéro')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date de dernière modification')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_mp_ids', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Moyen de Paiment',
                'verbose_name_plural': 'Moyens de Paiment',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(default='useravatar.png', upload_to='profile/')),
                ('birth_date', models.DateField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
