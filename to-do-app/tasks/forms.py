from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['owner']  # Includes all fields from the Task model
    deadline = forms.DateField(widget=forms.DateInput(attrs= {'type':'date'}))
