from multiprocessing import AuthenticationError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login

def index(request):
    return render(request, 'manejador_basicas/templates/login.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationError(request, request.POST)
        if form.is_valid():
            # Lógica de inicio de sesión aquí
            user = form.get_user()
            login(request, user)  # Autenticar al usuario y establecer la sesión
            # Puedes redirigir a la página que desees después del inicio de sesión
            return HttpResponseRedirect('/manejador_basicas/templates/index/')  # Cambia '/dashboard/' por la URL deseada