from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('/facturacion/', include('facturacion.urls')),
    path('health/', views.health_check, name='health'),
]
