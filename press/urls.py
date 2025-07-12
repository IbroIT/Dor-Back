from django.urls import path
from .views import PressReleaseList, PopularPressReleaseList

urlpatterns = [
    path('', PressReleaseList.as_view(), name='press-release-list'),
    path('popular/', PopularPressReleaseList.as_view(), name='popular-press-releases'),
]