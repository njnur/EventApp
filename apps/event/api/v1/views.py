from .serializers import EventSerializer
from apps.event.models import Event

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet


class AccountViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing the events
    """
    PAGE_SIZE = 5

    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    queryset = Event.objects.all()
