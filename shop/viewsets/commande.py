from requests import Response
from rest_framework import viewsets
from shop.models.commande import CommandeModel
from shop.serializers.commande import CommandeModelSerializer

class CommandeModelViewSet(viewsets.ModelViewSet):
    queryset = CommandeModel.objects.all()
    serializer_class = CommandeModelSerializer
   

    def valideCommande(self):
        user = self.request.user
        if user.groups.filter(name='vendeur').exists():
            return CommandeModel.objects.filter(products__seller=user.vendeur).distinct()
        return CommandeModel.objects.none()

    def perform_update(self, serializer):
        serializer.save(status='validated')