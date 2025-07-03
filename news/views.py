from rest_framework import viewsets
from .models import News, NewsCategory
from .serializers import NewsSerializer, NewsCategorySerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-published_date')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']

class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer