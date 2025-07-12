from django.urls import path
from .views import FeaturedNewsList, NewsList

urlpatterns = [
    path('featured/', FeaturedNewsList.as_view(), name='featured-news'),
    path('', NewsList.as_view(), name='news-list'),
]