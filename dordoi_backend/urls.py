from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', include('news.urls')),
    path('api/press-releases/', include('press.urls')),
    path('api/archive/', include('archive.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)