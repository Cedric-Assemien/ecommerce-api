from rest_framework import viewsets
from shop.models.panier import PanierModel
from shop.serializers.panier import PanierModelSerializer

class PanierModelViewSet(viewsets.ModelViewSet):
    queryset = PanierModel.objects.all()
    serializer_class = PanierModelSerializer