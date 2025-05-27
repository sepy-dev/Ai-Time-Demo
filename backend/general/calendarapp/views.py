from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer



# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import dateparser
from datetime import datetime, timedelta
import pytz



class ParseEventTime(APIView):
    def post(self, request):
        content = request.data.get('content', '')
        now = datetime.now(pytz.UTC)

        start = dateparser.parse(content, settings={'RELATIVE_BASE': now})
        if start is None:
            return Response({'error': 'زمانی پیدا نشد'}, status=400)

        end = start + timedelta(hours=1)  # فرض: تسک‌ها پیش‌فرض 1 ساعته‌ان

        return Response({
            'start': start.isoformat(),
            'end': end.isoformat()
        }, status=200)
