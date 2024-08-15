from django.shortcuts import render

def index(request):
    """Main page for learning_logs"""
    return render(request, 'learning_logs/index.html')
