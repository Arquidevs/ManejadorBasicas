from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('crear_factura/', views.crear_factura, name='crear_factura')
]