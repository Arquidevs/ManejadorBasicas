from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'manejador_basicas/templates/login.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm(request)

    return render(request, 'manejador_basicas/templates/login.html', {'form': form})

def dashboard_view(request):
    return render(request, 'manejador_basicas/templates/index.html')