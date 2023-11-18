from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('measurements/', include('measurements.urls')),
    path('variable-list/', include('variables.urls')),  
]







