from rest_framework import viewsets
from shop.models.produit_commande import ProduitCommandeModel
from shop.serializers.produit_commande import ProduitCommandeModelSerializer

class ProduitCommandeModelViewSet(viewsets.ModelViewSet):
    queryset = ProduitCommandeModel.objects.all()
    serializer_class = ProduitCommandeModelSerializer