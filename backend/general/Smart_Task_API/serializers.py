# serializers.py
from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    end = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'content', 'start', 'end']
