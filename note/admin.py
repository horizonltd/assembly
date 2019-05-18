from django.contrib import admin
from . models import  Note
# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(Note, NoteAdmin)