
from django.contrib import admin
from django.urls import path, include
from .views import login
# from .views import login, sample_api
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/downlaods/', include('downlaods.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/conference/', include('conference.urls')),
    path('api/login', login),
    path('api/attendees/', include('attendees.urls')),
    path('api/note/', include('note.urls')),
  
    # path('api/sampleapi', sample_api),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]