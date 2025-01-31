from rest_framework import viewsets
from customer.models.adresse_de_livraison import AdresseModel
from customer.serializers.adresse_de_livraison import AdresseModelSerializer

class AdresseModelViewSet(viewsets.ModelViewSet):
    queryset = AdresseModel.objects.all()
    serializer_class = AdresseModelSerializer
    
    def valideAdresse(self):
        return AdresseModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)