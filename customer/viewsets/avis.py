from requests import Response
from rest_framework import viewsets
from customer.models.avis import AvisModel
from customer.serializers.avis import AvisModelSerializer
from boutique.models.produit import ProduitModel

class AvisModelViewSet(viewsets.ModelViewSet):
    queryset = AvisModel.objects.all()
    serializer_class = AvisModelSerializer
    
    def creerAvis(self, request, *args, **kwargs):
        produit = ProduitModel.objects.get(pk=request.data['product_id'])
        commentaire = AvisModel.objects.create(
            user=request.user,
            product=produit,
            text=request.data['text']
        )
        return Response({'status': 'comment added','created': commentaire},)