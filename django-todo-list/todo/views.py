from django.http import HttpResponseNotAllowed, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import TodoModelForm, DeleteConfirmForm


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

@login_required
def new(request):
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        todo =form.save(commit=False)
        todo.creator = request.user
        todo.creator = request.user
        todo.save()
        return redirect('todo:index')

    return render(request, 'todo/new.html', {'form': form})

@login_required
def show(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo/show.html', {'todo': todo})

@login_required
def edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoModelForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save(commit=False)
        todo.creator = request.user
        todo.save()
        return redirect('todo:show', pk)

    return render(request, 'todo/edit.html', {'form': form})

@login_required
def delete(request, pk):
    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid() and form.cleaned_data['check']:
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return render(request, 'todo/index.html', {'todo': todo})

    return render(request, 'todo/delete.html', {'form': form})
