from rest_framework import serializers
from boutique.models.tag import TagModel

class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ['id', 'nom', 'active', 'created_at', 'updated_at']