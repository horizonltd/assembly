from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
       

#Event Model
class Conference(models.Model):
    featured_image = models.ImageField(default='')
    conference_paper = models.CharField(max_length=100, default='')
    conference_title = models.CharField(max_length=100, default='')
    upload_paper = models.FileField()
    proceeding_paper_title = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    speaker_name = models.CharField(max_length=100, default='')
    other_authors = models.CharField(max_length=100, default='')
    conference_location = models.CharField(max_length=100, default='')
    sponsor = models.CharField(max_length=100, default='')
    conference_start_date = models.DateField(default=2019-12-13)
    conference_end_date = models.DateField(default=2019-12-13)
    place_of_publication = models.CharField(blank=True, max_length=100)
    online_link = models.URLField(default='')
    latitude = models.CharField(max_length=150, default='')
    longitude = models.CharField(max_length=150, default='')
    
    def __str__(self):
        return self.conference_paper


#AGENDA REQUIREMENTS
class Agenda(models.Model):

    event = models.ForeignKey(Conference, related_name='agendas', on_delete=models.CASCADE, default='')
    documentary_on_cpn = models.CharField(max_length=255)
    order_of_agenda = models.IntegerField()
    arrival_and_registraion = models.CharField(max_length=255)
    induction_programme = models.CharField(max_length=255)
    welcome_address = models.CharField(max_length=255)
    induction_lectures = models.CharField(max_length=255)
    induction_of_new_members = models.CharField(max_length=255)
    welcome_address_by_president = models.CharField(max_length=150)
    remarks = models.CharField(max_length=200)
    photograph = models.CharField(max_length=255)
    documentary_on_cpn = models.CharField(max_length=255)
    lunch = models.CharField(max_length=255)
    annual_general_meeting = models.CharField(max_length=255)
    dinner_and_presentation_of_awards_and_certificate = models.CharField(max_length=255)



        
    class Meta:
        unique_together = ('event', 'order_of_agenda')
        ordering = ['order_of_agenda']

    def __str__(self):
        return '%d: %s' % (self.order_of_agenda, self.event)

    # def __str__(self):
    #     return self.conference_title
