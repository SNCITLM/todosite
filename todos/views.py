from django.shortcuts import render
from django.http import HttpResponse


# This views renders all of the current todos on screen.
def index(request):
    return HttpResponse("Hello, world. You're at the todos index.")

def edit(request, todo_id):
    return HttpResponse('Hey, you want to edit todo %s' % todo_id)
