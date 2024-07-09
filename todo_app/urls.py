from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name= 'home'),
    path('create/', views.TaskCreateView.as_view(), name= 'create'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name= 'delete'),
]