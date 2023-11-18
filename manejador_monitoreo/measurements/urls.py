from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('measurement/', views.measurement_list, name='measurement'),
    path('measurementcreate/', csrf_exempt(views.measurement_create), name='measurementCreate'),
]
