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

@login_required    
def task_detail(request,task_id):
    task=get_object_or_404(Task,id=task_id,user=request.user)
    return render(request,'tasks/task_detail.html',{'task':task})

@login_required
def task_edit(request,task_id):
    task=get_object_or_404(Task,id=task_id,user=request.user)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'✅ Task updated!')
            return redirect('task_detail',task_id=task.id)
    else:
        form=TaskForm(instance=task)
    return render(request,'tasks/task_form.html',{'form':form,'title':'Edit Task'})    

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, '✅ Task deleted!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})