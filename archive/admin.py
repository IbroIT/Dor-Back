from django.contrib import admin
from .models import NewsItem, NewsCategory
from django.utils.html import format_html

class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image_preview', 'views', 'is_featured')
    list_filter = ('categories', 'date', 'is_featured')
    search_fields = ('title', 'excerpt', 'content')
    date_hierarchy = 'date'
    filter_horizontal = ('categories',)
    readonly_fields = ('views', 'image_preview')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'excerpt', 'content', 'date')
        }),
        ('Изображение', {
            'fields': ('image', 'image_preview')
        }),
        ('Категории и настройки', {
            'fields': ('categories', 'is_featured')
        }),
        ('Статистика', {
            'fields': ('views',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
        return "Нет изображения"
    image_preview.short_description = 'Превью'

    # Действия для админки
    actions = ['mark_as_featured', 'mark_as_not_featured']
    
    @admin.action(description='Пометить как избранное')
    def mark_as_featured(self, request, queryset):
        queryset.update(is_featured=True)
    
    @admin.action(description='Снять отметку "избранное"')
    def mark_as_not_featured(self, request, queryset):
        queryset.update(is_featured=False)

admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)