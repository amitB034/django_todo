from django.db import models
from django.utils import timezone
from django.conf import settings

class Tasks(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=64)
    task_due = models.DateTimeField(verbose_name='Due Date')
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    
    def __str__(self):
        return self.task_title