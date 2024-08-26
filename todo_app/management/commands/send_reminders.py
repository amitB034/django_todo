from django.core.management.base import BaseCommand
from django.utils import timezone
from todo_app.models import Tasks

class Command(BaseCommand):
    help = 'Send reminders for tasks'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        tasks_to_remind = Tasks.objects.filter(reminder_date__lte=now, is_completed=False)
        for task in tasks_to_remind:
            self.stdout.write(f'Reminder: {task.title}')
            task.reminder_date = None
            task.save()