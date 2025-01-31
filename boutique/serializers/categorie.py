from rest_framework import serializers
from boutique.models import CategorieModel

class CategorieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieModel
        fields = ['id', 'nom', 'decsription', 'active', 'created_at', 'updated_at']