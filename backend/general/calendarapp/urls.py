from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, ParseEventTime

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('time/', ParseEventTime.as_view(), name='time'),
]


