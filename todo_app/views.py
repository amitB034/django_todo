from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse

from .models import Tasks
from .form import TaskCreationForm

# def homepage(request):
#     return render(request, 'home.html')

class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        queryset = Tasks.objects.all().order_by('-created_at')
        return queryset
    
class TaskCreateView(CreateView):
    model = Tasks
    form_class = TaskCreationForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('todo_app:home')

    def form_valid(self, form):
        pd = form.save(commit=False)
        pd.user = self.request.user
        pd.save()
        return super().form_valid(form)
    
class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = 'delete.html'
    success_url = reverse_lazy('todo_app:home')

    def get(self, request, *args, **kwargs):
        # オブジェクトを取得して削除
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())