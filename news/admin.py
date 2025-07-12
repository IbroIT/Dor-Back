from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_type', 'date_published', 'is_active')
    list_filter = ('news_type', 'is_active')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}