from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login

# Create your views here.
def Sign_upView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful! You can now log in.")
            login(request,user)
            return redirect("tasks:display_tasks")
    else:
        form = UserCreationForm()
    context = {"form":form}
    return render(request,'accounts/register.html',context)
def home(request):
    return render(request,'accounts/home.html')
