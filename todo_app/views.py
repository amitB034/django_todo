from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse

def homepage(request):
    print("l")

    return render(request, 'home.html')