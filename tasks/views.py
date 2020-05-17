from django.shortcuts import render, redirect
from .models import Task
from .forms import *
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView




def home(request):
    tasks = Task.objects.all()
    context  = {'tasks': tasks}


    return render(request, 'tasks/todo.html', context)



class TodoDetail(DetailView):
    model = Task
    template_name = 'tasks/detail-todo.html'


class CreateTodo(CreateView):

    model = Task
    template_name = 'tasks/create-todo.html'
    fields = ['title', 'name']


class UpdateTodo(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    fields = ['title', 'name']



class DeleteTodo(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = '/'
