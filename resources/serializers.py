from rest_framework import serializers
#from hub.models import Lecture
from .import models

# Serializers
class DownloadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Downloads
        fields = ('File_Title','File','Author','File_Description')