from django.shortcuts import render,get_object_or_404,redirect
from .models import Topic
from django import http
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import Http404

def home(request):
    return render(request,'fullstack temps/home.html')
@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'fullstack temps/topics.html', context)
@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    # Make sure the topic belongs to the current user.
    check_topic_owner(topic,request)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'fullstack temps/topic.html', context)
@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)  # Do not save to the database yet
            new_topic.owner = request.user      # Set the owner to the currently logged-in user
            new_topic.save()
            return redirect('fullstack:topics')
        # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'fullstack temps/new_topic.html', context)
@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic,request)

    if request.method != 'POST':
        form = EntryForm()
    else:
    # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('fullstack:topic', topic_id=topic_id)
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'fullstack temps/new_entry.html', context)
def delete_topic(request,topic_id):
    topic = Topic.objects.get(id = topic_id)
    topic.delete()
    return redirect('fullstack:topics')
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic,request)

    if request.method != 'POST':
    # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
    # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('fullstack:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'fullstack temps/edit_entry.html', context)
def delete_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    id = entry.topic.id  # Retrieve the topic ID before deleting
    entry.delete()
    return redirect('fullstack:topic', id)

def check_topic_owner(topic,request):
    if topic.owner != request.user:
        raise Http404
from django.contrib.auth.models import User

def create_superuser():
    username = "admin"
    email = ""
    password = "dddd"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser {username} created successfully.")
    else:
        print(f"Superuser {username} already exists.")
