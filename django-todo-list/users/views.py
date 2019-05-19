from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user =form.save()
        login(request, user)
        return redirect('todo:index')

    return render(request, 'users/reqister.html', {'form':form})
