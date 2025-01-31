from rest_framework import viewsets
from boutique.models.produit import ProduitModel
from boutique.serializers.produit import ProduitModelSerializer

class ProduitModelViewSet(viewsets.ModelViewSet):
    queryset = ProduitModel.objects.all()
    serializer_class = ProduitModelSerializer