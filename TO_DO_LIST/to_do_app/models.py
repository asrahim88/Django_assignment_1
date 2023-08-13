from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskId = models.IntegerField(default=0, primary_key=True)
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)