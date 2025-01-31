from rest_framework import serializers
from shop.models.panier import PanierModel

class PanierModelSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = PanierModel
        fields = ['id', 'reference', 'user_id', 'active', 'created_at', 'updated_at', 'total']