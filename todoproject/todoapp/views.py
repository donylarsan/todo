from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todoform
from todoapp.models import Task

# class based view
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class TaskListview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'tk'


class TaskDetailsView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'prio', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvDetails', kwargs={'pk': self.object.id})



class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvList')

# Create your views here.

def add(request):
    tas = Task.objects.all()
    if request.method == 'POST':
        nam = request.POST.get('task', '')
        prior = request.POST.get('prio', '')
        dat = request.POST.get('date', '')
        tsk = Task(name=nam, prio=prior, date=dat)
        tsk.save()

    return render(request, 'index.html', {'tk': tas})


def delete(request, taskid):
    tk = Task.objects.get(id=taskid)
    if request.method == 'POST':
        tk.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    fo = Todoform(request.POST or None, instance=task)
    if fo.is_valid():
        fo.save()
        return redirect('/')

    return render(request, 'edit.html', {'f': fo, 'ta': task})
