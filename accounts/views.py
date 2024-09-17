from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import SignUpForm, LoginFrom

# class SignUpView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('accounts:login')
#     template_name = 'signup.html'

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class =SignUpForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('accounts:login')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context

class LoginView(LoginView):
    form_class = LoginFrom
    template_name = "login.html"

class LogoutView(LogoutView):
    success_url = reverse_lazy('todo_app:home')