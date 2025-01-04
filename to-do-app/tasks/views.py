from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from .models import Task  # Import specific model
from .forms import TaskForm # import form model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# View to display all tasks
@login_required(login_url='accounts:login')
def display_tasks(request):
    """
    Display a list of all tasks with optional search and completion status filters.
    """
    query = request.GET.get("q")
    tasks = Task.objects.filter(owner=request.user)  # Start with tasks owned by the user
    # Initialize state to None (or you could leave it uninitialized and only apply it when needed)
    state = None
    # Handle completion status filtering if 'query' is 'completed' or 'pending'
    if query:
        query = query.lower()
        if query == 'completed':
            state = True
        elif query == 'pending':
            state = False
        # Apply search and status filters if state is set
        tasks = tasks.filter(Q(title__icontains=query) |  Q(description__icontains=query) | 
        (Q(status=state) if state is not None else Q())
        )

    context = {"tasks": tasks}
    return render(request, 'tasks/all_tasks.html', context)
@login_required(login_url='accounts:login')
def create_tasks(request):
    """
    Create a list of tasks
    """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('tasks:display_tasks')
        else:
            # Display specific error messages for invalid form inputs
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = TaskForm()
    context = {"form":form}
    return render(request,'tasks/create_task.html',context)
@login_required(login_url='accounts:login')
def delete_tasks(request, pk="",ps =""):
    """
    A function to delete tasks
    """
    # This raises Http404 if the task doesn't exist
    if pk:
        task = get_object_or_404(Task, id=pk) 
    if request.method == 'POST':
        if ps:
            Task.objects.all().delete()
            messages.success(request, 'All Tasks successfully deleted!')

        else:
            task.delete()
            messages.success(request, 'Task successfully deleted!')

        return redirect('tasks:display_tasks')
    else:
        context = {'obj': task.title if pk else ps}
        return render(request, 'tasks/confirm.html', context)
@login_required(login_url='accounts:login')
def update_tasks(request,pk):
    task = get_object_or_404(Task,id = pk)
    if request.method == "POST":
        form = TaskForm(data=request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:display_tasks")

    else:
        form = TaskForm(instance=task)
    context = {'form': form,'task':task}
    return render(request,'tasks/update_task.html',context)

