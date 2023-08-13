from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.TaskModel
        exclude = ["is_completed"]
        
        widgets = {
            'taskId': forms.TextInput(attrs={'placeholder': 'Write Your Task Id', "class": " focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2"}),
            
            'taskTitle': forms.TextInput(attrs={'placeholder': 'Write Your Task name', "class": " focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2"}),
            
            'taskDescription': forms.Textarea(attrs={'placeholder': 'Write Your Task Description', "class": " focus:outline-cyan-200 focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2"})
            
            # Add other fields and their respective widgets here
        }