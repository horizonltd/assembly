from rest_framework import serializers
#from hub.models import Lecture
from .import models

class ConferenceSerializer(serializers.ModelSerializer):
    
    agendas = serializers.StringRelatedField(many=True)


    class Meta:

        model = models.Conference
        # fields = '__all__'
        fields = ('conference_paper', 'conference_title', 'upload_paper','proceeding_paper_title','author','speaker_name','other_authors',
        'conference_location','sponsor',
        'conference_start_date',
        'conference_end_date','place_of_publication','online_link','latitude','longitude','agendas')