from rest_framework import viewsets
from shop.models.commande import CommandeModel
from shop.serializers.commande import CommandeModelSerializer

class CommandeModelViewSet(viewsets.ModelViewSet):
    queryset = CommandeModel.objects.all()
    serializer_class = CommandeModelSerializer