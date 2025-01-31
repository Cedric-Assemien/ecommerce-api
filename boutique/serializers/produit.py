from rest_framework import serializers
from boutique.models import ProduitModel

class ProduitModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduitModel
        fields = ['id', 'nom', 'decsription', 'prix', 'sous_categorie_id', 'tag_ids', 'active', 'created_at', 'updated_at']