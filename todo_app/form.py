from django import forms
from .models import Tasks

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ("task_title", "task_due")
        widgets = {
            'task_due': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }