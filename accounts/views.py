from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"

class LogoutView(Base)