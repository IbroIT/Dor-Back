from django.urls import path
from .views import NewsArchiveView, NewsCategoriesView

urlpatterns = [
    path('archive/', NewsArchiveView.as_view(), name='news-archive'),
    path('categories/', NewsCategoriesView.as_view(), name='news-categories'),
]