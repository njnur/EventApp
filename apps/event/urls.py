from django.urls import path, include

from rest_framework import routers
from apps.event.api.v1.views import AccountViewSet

router = routers.SimpleRouter()


router.register(r'events', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
