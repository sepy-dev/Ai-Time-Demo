# urls.py
from django.urls import path
from .views import parse_time_view

urlpatterns = [
    path('parse-time/', parse_time_view),
]
