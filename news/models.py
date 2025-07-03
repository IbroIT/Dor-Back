from django.db import models
from django.utils import timezone

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title