from rest_framework import viewsets
from customer.models.moyen_de_paiement import MoyenoDePaiementModel
from customer.serializers.moyen_de_paiement import MoyenoDePaiementModelSerializer

class MoyenoDePaiementModelViewSet(viewsets.ModelViewSet):
    queryset = MoyenoDePaiementModel.objects.all()
    serializer_class = MoyenoDePaiementModelSerializer