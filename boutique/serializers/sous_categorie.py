from rest_framework import serializers
from boutique.models.sous_categorie import SousCategorieModel

class SousCategorieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousCategorieModel
        fields = ['id', 'nom', 'decsription', 'categorie_id', 'active', 'created_at', 'updated_at']