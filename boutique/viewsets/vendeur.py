from rest_framework import viewsets
from boutique.models.vendeur import VendeurModel
from boutique.serializers.vendeur import VendeurModelSerializer

class VendeurModelViewSet(viewsets.ModelViewSet):
    queryset = VendeurModel.objects.all()
    serializer_class = VendeurModelSerializer