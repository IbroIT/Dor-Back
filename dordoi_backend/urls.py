from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from news import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'news-categories', views.NewsCategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]