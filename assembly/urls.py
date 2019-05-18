
from django.contrib import admin
from django.urls import path, include
from .views import login
# from .views import login, sample_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/conference/', include('conference.urls')),
    path('api/login', login),
    path('api/attendees/', include('attendees.urls')),
    path('api/note/', include('note.urls')),
    # path('api/sampleapi', sample_api),
]