from django.db import models


class Tasks(models.Model):
    task_title = models.CharField(max_length=64)
    task_due = models.IntegerField()
    is_finished = models.BooleanField()
    
    def __str__(self):
        return self.task_title