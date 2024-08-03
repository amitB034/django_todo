from django.db import models
from django.utils import timezone
from django.conf import settings

class Tasks(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=64)
    task_due = models.DateTimeField(verbose_name='Due Date')
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    reminder_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # リマインダー日時を期限の1日前に設定
        if self.due_date and not self.reminder_date:
            self.reminder_date = self.due_date - timezone.timedelta(days=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.task_title