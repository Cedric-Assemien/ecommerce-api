from rest_framework import serializers
from boutique.models.vendeur import VendeurModel

class VendeurModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendeurModel
        fields = ['id', 'nom', 'admin_user_id', 'active', 'created_at', 'updated_at']