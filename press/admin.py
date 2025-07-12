from django.contrib import admin
from .models import PressRelease
from django.utils.html import format_html

class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'market', 'type_display', 'date_published', 'views', 'is_featured', 'image_preview')
    list_filter = ('market', 'type', 'is_featured', 'date_published')
    search_fields = ('title', 'summary', 'content')
    date_hierarchy = 'date_published'
    ordering = ('-date_published',)
    readonly_fields = ('views', 'image_preview')
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'summary', 'content', 'market', 'type')
        }),
        ('Медиа', {
            'fields': ('image', 'image_preview')
        }),
        ('Даты и статистика', {
            'fields': ('date_published', 'views', 'is_featured')
        }),
        ('Контактная информация', {
            'fields': ('contact_name', 'contact_position', 'contact_phone', 'contact_email')
        }),
    )

    def type_display(self, obj):
        return obj.get_type_display()
    type_display.short_description = 'Тип релиза'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Превью изображения'

admin.site.register(PressRelease, PressReleaseAdmin)