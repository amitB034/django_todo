from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
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
        user = self.request.user
        if user.is_authenticated:
            return Tasks.objects.filter(user=user, is_finished=False).order_by('-created_at')
        else:
            return Tasks.objects.none()
    
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
    success_url = reverse_lazy('todo_app:task_done')

    def get(self, request, *args, **kwargs):
        # オブジェクトを取得して削除
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())
    
class MarkChangeView(UpdateView):
    model = Tasks
    fields = ['is_finished']
    template_name = 'mark_ch.html'
    success_url = reverse_lazy('todo_app:home')

    def post(self, request, *args, **kwargs):
        # task = self.get_object()
        # if 'is_finished' in request.POST:
        #     task.is_finished = True
        #     task.save()
        task = self.get_object()
        print(task)
        if 'is_finished' in request.POST:
            task.is_finished = request.POST['is_finished']
            task.save()
        return HttpResponseRedirect(self.success_url)

class TaskDoneView(ListView):
    template_name = 'task_done.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Tasks.objects.filter(user=user, is_finished=True)
        else:
            return Tasks.objects.none()