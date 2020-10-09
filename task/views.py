from django.shortcuts import render, redirect, HttpResponse
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login
from .models import Task
from django.contrib.auth.decorators import login_required


def index(request):
    tasks = None
    if request.user.is_authenticated:
        tasks = request.user.task_set.all()
        # print(tasks)
    context = {'tasks': tasks}
    return render(request, 'task/index.html', context)


def about(request):
    return render(request, 'task/about.html')

def addTask(request):
    if request.method == 'POST':
        task_name = request.POST['task_name']
        task = Task(task_name=task_name)
        task.save()
        # add to user
        request.user.task_set.add(task)
    return redirect('index')

def removeTask(request, task_id):
    try:
        if request.user.is_authenticated:
            task = Task.objects.get(pk=task_id)
            request.user.task_set.remove(task)
    except:
        pass
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'registration/registration.html', context)

@login_required
def profile(request):
    return render(request, 'task/profile.html')