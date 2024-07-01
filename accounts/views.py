from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import SignUpForm, LoginFrom

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class LoginView(LoginView):
    form_class = LoginFrom
    template_name = "login.html"

class LogoutView(LogoutView):
    success_url = reverse_lazy("todo_app:home")