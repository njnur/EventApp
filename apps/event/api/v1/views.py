from .serializers import EventSerializer
from apps.event.models import Event
from .services import CustomPagination

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class AccountViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing the events
    """
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
    pagination_class = CustomPagination
