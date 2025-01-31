from rest_framework import viewsets
from shop.models.produit_panier import ProduitPanierModel
from shop.serializers.produit_panier import ProduitPanierModelSerializer

class ProduitPanierModelViewSet(viewsets.ModelViewSet):
    queryset = ProduitPanierModel.objects.all()
    serializer_class = ProduitPanierModelSerializer