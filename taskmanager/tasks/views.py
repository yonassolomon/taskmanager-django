from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks=Task.objects.filter(user=request.user)
    return render(request,'tasks/task_list.html',{'tasks':tasks})

@login_required
def task_create(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
            messages.success(request,'✅ Task created!')
            return redirect('task_list')
    else:
        form=TaskForm()
    return render(request,'tasks/task_form.html',{'form':form,'title':'New Task'})    
