from django.urls import path
from . import views

#This bind the views created in views.py class of the hub
urlpatterns = [

    #members
    path('', views.NoteList.as_view()),
    path('<int:pk>/', views.NoteDetail.as_view()), #This get the ID of the passed lecture

]
