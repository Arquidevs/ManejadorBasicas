from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'manejador_basicas/templates/index.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)

class LoginCustomView (LoginView):
    form_class = AuthenticationForm
    template_name='registration/login.html'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Inicio de sesión exitoso
            login(request, form.get_user())
            return redirect('manejador_basicas/templates/index.html')  # Redirige a la página 'index'
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})