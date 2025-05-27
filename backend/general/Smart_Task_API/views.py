# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import parse_time_from_content

@api_view(['POST'])
def parse_time_view(request):
    content = request.data.get('content')
    title = request.data.get('title', 'بدون عنوان')

    if not content:
        return Response({'error': 'فیلد content الزامی است.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        start, end = parse_time_from_content(content)
        return Response({
            'title': title,
            'start': start.strftime('%Y-%m-%d %H:%M'),
            'end': end.strftime('%Y-%m-%d %H:%M')
        })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

