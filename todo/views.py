from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect

def index(request):    
    todo_list = Todo.objects.order_by("id")    

    form = TodoForm()
    context = {"todo_list":todo_list, "form":form}

    return render(request, "todo/index.html", context)

def add_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=form.cleaned_data["text"])
        new_todo.save()
        
    return HttpResponseRedirect("/")

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = True
    todo.save()

    return HttpResponseRedirect("/")

def delete_completed(request):
    Todo.objects.filter(complete=True).delete()

    return HttpResponseRedirect("/")

def delete_all(request):
    Todo.objects.all().delete()
    
    return HttpResponseRedirect("/")