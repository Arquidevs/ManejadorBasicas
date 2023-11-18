from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('measurements/', include('measurements.urls')),
    path('variables/', include('variables.urls')),
]






