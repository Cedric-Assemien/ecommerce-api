from rest_framework import viewsets
from boutique.models.tag import TagModel
from boutique.serializers.tag import TagModelSerializer

class TagModelViewSet(viewsets.ModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = TagModelSerializer