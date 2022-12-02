from apps.event.models import Event

from rest_framework.serializers import ModelSerializer


class EventSerializer(ModelSerializer):
    """
    Model serializer for table Event
    """
    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'date']
