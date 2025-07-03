from django.contrib import admin
from .models import News, NewsCategory
from django.utils.html import format_html

class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

def toggle_published(modeladmin, request, queryset):
    for item in queryset:
        item.is_published = not item.is_published
        item.save()
toggle_published.short_description = "Переключить статус публикации"

class NewsAdmin(admin.ModelAdmin):
    actions = [toggle_published]
    list_display = ('title', 'category', 'published_date', 'is_published', 'image_preview')
    list_filter = ('category', 'published_date', 'is_published')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
    readonly_fields = ('image_preview',)
    list_display = ('title', 'category', 'published_date', 'is_published', 'image_preview')
    list_filter = ('category', 'published_date', 'is_published')  # Добавить в фильтры
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'image')
        }),
        ('Содержание', {
            'fields': ('excerpt', 'content')
        }),
        ('Дата публикации', {
            'fields': ('published_date',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px;"/>', obj.image.url)
        return "Нет изображения"
    image_preview.short_description = "Превью"

admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(News, NewsAdmin)