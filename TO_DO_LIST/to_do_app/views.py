from django.shortcuts import render, redirect
from . import models
from . import task_form

# Create your views here.
def show_task(request):
    data = models.TaskModel.objects.all()
    
    return render(request, 'show_task.html', {"data": data})

def add_task(request):
    if request.method == "POST":
        form = task_form.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = task_form.TaskForm()
    return render(request, 'add_task.html', {"form": form})

def complete_task(request):
    return render(request, 'complete_task.html')

def delete_task(request, id):
    data = models.TaskModel.objects.get(pk = id).delete()
    return redirect("show")

def delete_complete_task(request, id):
    data = models.TaskModel.objects.get(pk = id).delete()
    return redirect("all_complete")

def edit_task(request, id):
    edit_data = models.TaskModel.objects.get(pk = id)
    form = task_form.TaskForm(instance = edit_data)
    if request.method == "POST":
        form = task_form.TaskForm(request.POST, instance=edit_data)
        if form.is_valid():
            form.save()
            return redirect("show")
    return render(request, 'add_task.html', {"form": form})

def all_complete_task(request):
    data = models.TaskModel.objects.all()
    return render(request, 'complete_task.html', {"data": data})

def complete_task(request, id):
    complete = models.TaskModel.objects.get(pk = id) 
    complete.is_completed = True
    complete.save()
    return redirect("all_complete")
    

    