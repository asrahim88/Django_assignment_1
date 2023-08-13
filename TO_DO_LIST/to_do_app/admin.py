from django.contrib import admin
from . import models
# Register your models here.
class TaskModelRegister(admin.ModelAdmin):
    list_display = ("taskId","taskTitle", "taskDescription", "is_completed")

admin.site.register(models.TaskModel, TaskModelRegister)