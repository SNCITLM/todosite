from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from dateutil.parser import parse
from .models import Todo

# This views renders all of the current todos on screen.
def index(request):
    all_todos = Todo.objects.all()
    context = { 'todo_list': all_todos }
    return render(request, 'todos/index.html', context)

def edit(request, todo_id):
    current_todo = get_object_or_404(Todo, pk = todo_id)
    if request.method == 'POST':
        return update_todo(request, current_todo)
    else:
        return render(request, 'todos/edit.html', {'todo': current_todo})

def about(request):
    return HttpResponse("This site was created by Leonardo Hahn and Max Franke.")

def update_todo(request, todo):
    new_description = request.POST['description']
    if len(new_description) == 0:
        return render(request, 'todos/edit.html', {
            'todo': todo,
            'error_message': "Description can't be empty.",
        })

    new_due_date = request.POST['due_date']
    if len(new_due_date) == 0:
        return render(request, 'todos/edit.html', {
            'todo': todo,
            'error_message': "Due Date cannot be empty.",
        })

    new_progress = request.POST['progress']
    if len(new_progress) == 0 or 0 > int(new_progress) > 100:
        return render(request, 'todos/edit.html', {
            'todo': todo,
            'error_message': "Progress can't be empty and should be a percentage.",
        })

    try:
        todo.due_date = parse(new_due_date)
    except ValueError:
       return render(request, 'todos/edit.html', {
            'todo': todo,
            'error_message': "Invalid date.",
        })

    todo.description = new_description
    todo.progress = new_progress

    todo.save()

    return HttpResponseRedirect(reverse('todos:index'))

def delete(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect(reverse('todos:index'))

def new(request):
    if request.method == 'POST':
        return new_todo(request)
    else:
        return render(request, 'todos/new.html')

def new_todo(request):
    new_description = request.POST['description']
    if len(new_description) == 0:
        return render(request, 'todos/new.html', {
            'error_message': "Description can't be empty",
        })

    new_due_date = request.POST['due_date']
    if len(new_due_date) == 0:
        return render(request, 'todos/new.html', {
            'error_message': "Due Date can't be empty",
        })

    try:
        parsed_due_date = parse(new_due_date)
    except ValueError :
       return render(request, 'todos/new.html', {
            'error_message': "Invalid Date",
        })

    new_todo = Todo(description=new_description,due_date=parsed_due_date)
    new_todo.save()
    return HttpResponseRedirect(reverse('todos:index'))
