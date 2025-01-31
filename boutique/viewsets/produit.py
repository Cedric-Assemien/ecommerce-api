from rest_framework import viewsets
from boutique.models.produit import ProduitModel
from boutique.serializers.produit import ProduitModelSerializer

class ProduitModelViewSet(viewsets.ModelViewSet):
    queryset = ProduitModel.objects.all()
    serializer_class = ProduitModelSerializer
    
    def valideProduit(self):
        user = self.request.user
        if user.groups.filter(name='vendeur').exists():
            return ProduitModel.objects.filter(vendeur=user.vendeur)
        return ProduitModel.objects.none()

    def perform_create(self, serializer):
        serializer.save(vendeur=self.request.user.vendeur)