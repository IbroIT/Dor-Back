from django.db import models

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='news/')
    categories = models.ManyToManyField(NewsCategory)
    views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title