from rest_framework import serializers
from customer.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'telephone', 'image', 'birth_date']