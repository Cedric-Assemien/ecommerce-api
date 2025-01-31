from rest_framework import serializers
from shop.models import ProduitCommandeModel

class ProduitCommandeModelSerializer(serializers.ModelSerializer):
    total_ligne = serializers.ReadOnlyField()

    class Meta:
        model = ProduitCommandeModel
        fields = ['id', 'produit_id', 'commande_id', 'quantite', 'active', 'created_at', 'updated_at', 'total_ligne']