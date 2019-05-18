from django.db import models
from  attendees.models import Members
from  attendees.models import Members

# Create your models here.
# Models
class Note(models.Model):
    title = models.CharField(max_length=200, default='')
    content = models.TextField(max_length=200, default='')
    # default=2019-12-13

    def __str__(self):

        return self.title

