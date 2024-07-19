from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import SearchHistory


@api_view(['GET'])
def city_search_frequency(request):
    '''Показывает сколько раз вводили какой город'''
    frequency = SearchHistory.objects.values(
        'city').annotate(count=Count('city')).order_by('-count')
    return Response(frequency)
