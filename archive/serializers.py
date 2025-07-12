from rest_framework import serializers
from .models import NewsItem, NewsCategory

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['id', 'name', 'slug']

class NewsItemSerializer(serializers.ModelSerializer):
    categories = NewsCategorySerializer(many=True)
    
    class Meta:
        model = NewsItem
        fields = ['id', 'title', 'excerpt', 'content', 'date', 'image', 'categories', 'views', 'is_featured']