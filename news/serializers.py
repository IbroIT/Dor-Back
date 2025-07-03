from rest_framework import serializers
from .models import News, NewsCategory

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['id', 'name', 'slug']

class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer()
    
    class Meta:
        model = News
        fields = ['id', 'title', 'slug', 'content', 'excerpt', 'category', 'published_date', 'image']