from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# This views renders all of the current todos on screen.
def index(request):
    all_todos = Todo.objects.all()
    context = { 'todos': all_todos }
    return render(request, 'todos/index.html', context)

def edit(request, todo_id):
    return HttpResponse('Hey, you want to edit todo %s' % todo_id)

def about(request):
    return HttpResponse("This site was created by Leonardo Hahn and Max Franke")
