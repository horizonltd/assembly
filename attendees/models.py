from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


#Type of Membership
class TypeOfMembership(models.Model):
    Membership_Type = models.CharField(max_length=150)

    def __str__(self):
        return self.Membership_Type

class Members(models.Model):
    membership_registration_number = models.CharField(max_length=150, default='')
    surname = models.CharField(max_length=150, default='')
    First_name = models.CharField(max_length=150, default='')
    Other_names	= models.CharField(max_length=150, default='')
    address	= models.TextField(max_length=200, default='')
    phone_number = models.IntegerField(default='')
    email = models.EmailField()
    Payment_status = models.CharField(max_length=50, default='')
    entry_types = models.ForeignKey(TypeOfMembership, related_name='Member_Entry', on_delete=models.CASCADE, default='')

    class Meta:
        unique_together = ('First_name', 'phone_number')
        ordering = ['phone_number']

    def __str__(self):
        return '%d: %s' % (self.phone_number, self.First_name)


