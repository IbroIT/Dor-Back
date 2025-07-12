from rest_framework import generics
from .models import NewsItem, NewsCategory
from .serializers import NewsItemSerializer, NewsCategorySerializer

class NewsArchiveView(generics.ListAPIView):
    serializer_class = NewsItemSerializer
    queryset = NewsItem.objects.all().order_by('-date')

class NewsCategoriesView(generics.ListAPIView):
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.objects.all()