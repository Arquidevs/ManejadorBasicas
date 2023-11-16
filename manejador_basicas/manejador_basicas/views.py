from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'manejador_basicas/templates/index.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)