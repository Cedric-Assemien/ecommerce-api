from rest_framework import serializers
from customer.models import AvisModel

class AvisModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvisModel
        fields = ['id', 'titre', 'commentaire', 'user_id', 'produit_id', 'active', 'created_at', 'updated_at']