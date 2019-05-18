from rest_framework import generics
from . import models
from . import serializers

#Event views
class DownloadsList(generics.ListCreateAPIView):
    queryset  = models.Downloads.objects.all()
    serializer_class = serializers.DownloadsSerializer
class DownloadsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Downloads.objects.all()
    serializer_class = serializers.DownloadsSerializer