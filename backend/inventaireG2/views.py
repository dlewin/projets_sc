from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Yuze
from .serializers import YuzeSerializer

class YuzeViewSet(viewsets.ModelViewSet):
    queryset = Yuze.objects.all()
    serializer_class = YuzeSerializer
    permission_classes = [AllowAny]



