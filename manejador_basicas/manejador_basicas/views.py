from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect



def index(request):
    return render(request, 'manejador_basicas/templates/index.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)

class YourSignupView(View):
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Cambia 'home' al nombre de tu vista de inicio
        return render(request, self.template_name, {'form': form})      