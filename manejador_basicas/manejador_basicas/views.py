from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render(request, 'manejador_basicas/templates/login.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)
