from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    end = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Event
        fields = ['id', 'title', 'start', 'end']

