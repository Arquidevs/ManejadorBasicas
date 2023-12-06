from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('measurements/', include('measurements.urls')),
    path('variable-list/', include('variables.urls')),  
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]







