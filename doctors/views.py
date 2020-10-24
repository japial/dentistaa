from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate


def index(request: HttpRequest):
    return redirect('/')


def register(request: HttpRequest):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        return redirect('doctors/success')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def success(request: HttpRequest):
    return render(request, 'success.html')