from rest_framework import serializers
from shop.models.produit_panier import ProduitPanierModel

class ProduitPanierModelSerializer(serializers.ModelSerializer):
    total_ligne = serializers.ReadOnlyField()

    class Meta:
        model = ProduitPanierModel
        fields = ['id', 'produit_id', 'panier_id', 'quantite', 'active', 'created_at', 'updated_at', 'total_ligne']