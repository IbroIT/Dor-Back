from rest_framework import generics
from .models import PressRelease
from .serializers import PressReleaseSerializer

class PressReleaseList(generics.ListAPIView):
    queryset = PressRelease.objects.all()
    serializer_class = PressReleaseSerializer

class PopularPressReleaseList(generics.ListAPIView):
    queryset = PressRelease.objects.filter(is_featured=True).order_by('-views')[:5]
    serializer_class = PressReleaseSerializer