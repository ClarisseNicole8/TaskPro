from django.forms import ModelForm
from tasks.models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        exclude = ['is_completed']
