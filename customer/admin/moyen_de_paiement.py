from django.contrib import admin
from customer.models.moyen_de_paiement import MoyenoDePaiementModel


@admin.register(MoyenoDePaiementModel)
class MoyenoDePaiementModelAdmin(admin.ModelAdmin):
    list_display = ('type', 'carte', 'cvc', 'mois_expiration', 'annee_expiration', 'adresse_paypal', 'numero', 'user_id', 'active', 'created_at', 'updated_at')
    search_fields = ('type', 'user_id__username')
    fields = ('type', 'carte', 'cvc', 'mois_expiration', 'annee_expiration', 'adresse_paypal', 'numero', 'user_id', 'active')