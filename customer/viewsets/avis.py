from rest_framework import viewsets
from customer.models.avis import AvisModel
from customer.serializers.avis import AvisModelSerializer

class AvisModelViewSet(viewsets.ModelViewSet):
    queryset = AvisModel.objects.all()
    serializer_class = AvisModelSerializer