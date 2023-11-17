from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)

class LoginCustomView (LoginView):
    form_class = AuthenticationForm
    template_name='registration/login.html'
