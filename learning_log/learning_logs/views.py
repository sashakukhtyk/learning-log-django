from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm


def index(request):
    """Main page for learning_logs"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show single topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add new topic"""
    if request.method != 'POST':
        # Create an empty form, no data
        form = TopicForm()
    else:
        # Post method, prosed data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    # Show empty form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Add new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        # Got the data with a post method, prosed data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    # Show empty form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)