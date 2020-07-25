from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.

class TaskList(ListView):
    context_object_name = 'item_list'
    template_name = 'list.html'
    model = TodoModel

    def get_queryset(self): 
         return TodoModel.objects.order_by('duedate')

class TaskDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TaskCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('top')

class TaskDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('top')

class TaskUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('top')
    
    # def __init__(self, *args, **kwargs):
    #     super(TaskUpdate, self).__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs["class"] = "form-control"
