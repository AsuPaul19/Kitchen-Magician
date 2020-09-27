from kitchens.models import Kitchen
from rest_framework import viewsets, permissions
from .serializers import KitchenSerializer


#   Kitchen Viewset
class KitchenViewSet(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = KitchenSerializer
