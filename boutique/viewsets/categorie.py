from rest_framework import viewsets
from boutique.models.categorie import CategorieModel
from boutique.serializers.categorie import CategorieModelSerializer

class CategorieModelViewSet(viewsets.ModelViewSet):
    queryset = CategorieModel.objects.all()
    serializer_class = CategorieModelSerializer