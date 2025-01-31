from rest_framework import serializers
from customer.models.adresse_de_livraison import AdresseModel

class AdresseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdresseModel
        fields = ['id', 'ville', 'quartier', 'rue', 'longitude', 'latitude', 'indication', 'user_id', 'active', 'created_at', 'updated_at']