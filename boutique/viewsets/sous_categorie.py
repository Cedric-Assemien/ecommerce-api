from rest_framework import viewsets
from boutique.models.sous_categorie import SousCategorieModel
from boutique.serializers.sous_categorie import SousCategorieModelSerializer

class SousCategorieModelViewSet(viewsets.ModelViewSet):
    queryset = SousCategorieModel.objects.all()
    serializer_class = SousCategorieModelSerializer