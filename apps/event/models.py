from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Event(BaseModel):
    name = models.TextField(verbose_name=_('Event Name'))
    location = models.CharField(verbose_name=_('Event Location'), max_length=100)
    date = models.DateTimeField(verbose_name=_('Event Date'))

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-id']

    def __str__(self):
        return self.name
