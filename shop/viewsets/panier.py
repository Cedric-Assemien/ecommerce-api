from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from boutique.models.produit import ProduitModel
from shop.models.panier import PanierModel
from shop.serializers.panier import PanierModelSerializer

class PanierModelViewSet(viewsets.ModelViewSet):
    queryset = PanierModel.objects.all()
    serializer_class = PanierModelSerializer
    
    @action(detail=True, methods=['post'])
    def ajouter_panier(self, request, pk=None):
        product = ProduitModel.objects.get(pk=pk)
        panier, created = ProduitModel.objects.get_or_create(user=request.user)
        panier.products.add(product)
        panier.save()
        return Response({'status': 'product added to cart', 'created': created})