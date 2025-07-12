from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class News(models.Model):
    TYPES = (
        ('featured', 'Главная новость'),
        ('ordinary', 'Обычная новость'),
    )

    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Содержание')
    short_description = models.CharField('Краткое описание', max_length=300)
    image = models.ImageField(upload_to='news_images/', default='')
    news_type = models.CharField('Тип новости', max_length=10, choices=TYPES, default='ordinary')
    date_published = models.DateTimeField('Дата публикации', default=timezone.now)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date_published']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title