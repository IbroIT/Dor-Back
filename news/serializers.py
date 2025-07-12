from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'short_description', 'content', 'image', 
                 'news_type', 'date_published', 'slug', 'is_active']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None