from django.db import models
from django.utils import timezone

class PressRelease(models.Model):
    TYPE_CHOICES = [
        ('announcement', 'Анонс'),
        ('event_results', 'Итоги мероприятий'),
        ('new_project', 'Новые проекты'),
        ('partnership', 'Партнерства'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    summary = models.CharField(max_length=300, verbose_name="Краткое описание")
    image = models.ImageField(upload_to='press_releases/', verbose_name="Изображение")
    market = models.CharField(max_length=100, verbose_name="Рынок")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Тип")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    views = models.PositiveIntegerField(default=0, verbose_name="Просмотры")
    is_featured = models.BooleanField(default=False, verbose_name="Популярный")
    
    contact_name = models.CharField(max_length=100, verbose_name="Контактное лицо")
    contact_position = models.CharField(max_length=100, verbose_name="Должность")
    contact_phone = models.CharField(max_length=20, verbose_name="Телефон")
    contact_email = models.EmailField(verbose_name="Email")
    
    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Пресс-релиз'
        verbose_name_plural = 'Пресс-релизы'
    
    def __str__(self):
        return self.title