from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from django.db.models import F

# Create your views here.

class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"

class TodoDetail(DetailView):
    model = Todo
    context_object_name = "task"

class TodoCreate(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy("list")

class TodoUpdate(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    model = Todo
    context_object_name = 'task'
    success_url = reverse_lazy('list')

def events(request):
    events_data = Todo.objects.all().values('title', start=F('deadline'))
    events_data = list(events_data)

    return JsonResponse(events_data, safe=False)
