from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django_filters.rest_framework import DjangoFilterBackend

class FeaturedNewsList(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.filter(news_type='featured', is_active=True).order_by('-date_published')[:5]

    def get_serializer_context(self):
        return {'request': self.request}

class NewsList(generics.ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.filter(is_active=True).order_by('-date_published')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['news_type']

    def get_serializer_context(self):
        return {'request': self.request}