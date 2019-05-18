from rest_framework import serializers
#from hub.models import Lecture
from .import models

# Serializers
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Note
        fields = ('title','content')
