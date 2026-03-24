from rest_framework.viewsets import ModelViewSet
from core.models.cor import Cor 
from core.serializers import CorSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer