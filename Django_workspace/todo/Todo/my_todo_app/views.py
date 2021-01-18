from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo

# MVC 패턴의 Controller 역할

# my_todo_app/
def index(request) :
    todos = Todo.objects.all()
    context = { "todos" : todos }
    return render(request, 'my_todo_app/index.html', context)

# my_todo_app/createTodo/
def createTodo(request) :
    todoContent = request.POST['todoInput']
    new_todo = Todo(content= todoContent)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))


# my_todo_app/deleteTodo/
def deleteTodo(request) :
    delete_todo_id = request.GET['id']
    todo = Todo.objects.get(id= delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))

# my_todo_app/clearTodo/
def clearTodo(request) :
    todos = Todo.objects.all()
    todos.delete()
    return HttpResponseRedirect(revers('index'))