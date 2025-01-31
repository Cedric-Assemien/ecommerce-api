from rest_framework import viewsets
from customer.models.profil import Profile
from customer.serializers.profil import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer