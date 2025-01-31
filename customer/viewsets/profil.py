from rest_framework import viewsets
from customer.models.profil import Profile
from customer.serializers.profil import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def valideProfil(self):
        return Profile.objects.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save()