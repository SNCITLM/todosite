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
    cur_todo = get_object_or_404(Todo, pk = todo_id)
    return render(request, 'todos/edit.html', {'todo': cur_todo})

def about(request):
    return HttpResponse("This site was created by Leonardo Hahn and Max Franke")

def save(request, todo_id):
    cur_todo = get_object_or_404(Todo, pk=todo_id)

    new_description = request.POST['description']
    if len(new_description) == 0:
        return render(request, 'todos/edit.html', {
            'todo': cur_todo,
            'error_message': "Description can't be empty",
    })

    new_due_date = request.POST['due_date']
    if len(new_due_date) == 0:
        return render(request, 'todos/edit.html', {
            'todo': cur_todo,
            'error_message': "Due Date can't be empty",
    })

    new_progress = request.POST['progress']
    if len(new_progress) == 0 or int(new_progress) < 0:
        return render(request, 'todos/edit.html', {
            'todo': cur_todo,
            'error_message': "Progress can't be empty or negtive",
    })

    try:
        cur_todo.due_date = parse(new_due_date)
    except ValueError :
       return render(request, 'todos/edit.html', {
            'todo': cur_todo,
            'error_message': "Invalid Date",
        })

    cur_todo.description = new_description
    cur_todo.progress = new_progress

    cur_todo.save()

    return HttpResponseRedirect(reverse ('todos:index'))

def delete(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect(reverse ('todos:index'))
