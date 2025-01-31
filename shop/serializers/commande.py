from rest_framework import serializers
from shop.models.commande import CommandeModel

class CommandeModelSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = CommandeModel
        fields = ['id', 'reference', 'date_de_commande', 'user_id', 'active', 'created_at', 'updated_at', 'total']