from django.forms import ModelForm
from django import forms
from .models import Task, SubTask, Priority

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        fields = "__all__"

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields= "__all__"
