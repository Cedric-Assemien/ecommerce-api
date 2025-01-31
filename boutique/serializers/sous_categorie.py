from rest_framework import serializers
from boutique.models import SousCategorieModel

class SousCategorieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SousCategorieModel
        fields = ['id', 'nom', 'decsription', 'categorie_id', 'active', 'created_at', 'updated_at']