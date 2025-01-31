from rest_framework import serializers
from customer.models import MoyenoDePaiementModel

class MoyenoDePaiementModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoyenoDePaiementModel
        fields = ['id', 'type', 'carte', 'cvc', 'mois_expiration', 'annee_expiration', 'adresse_paypal', 'numero', 'user_id', 'active', 'created_at', 'updated_at']