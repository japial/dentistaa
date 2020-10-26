from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .forms import UserSignUpForm


def index(request: HttpRequest):
    return redirect('/')


def register(request: HttpRequest):
    user_form = UserSignUpForm(request.POST)
    if user_form.is_valid():
        user = user_form.save()
        user.refresh_from_db()
        user.is_active = False
        user.save()
        return redirect('/doctors/success')
    else:
        user_form = UserSignUpForm()
    return render(request, 'registration.html', {'user_form': user_form})


def success(request: HttpRequest):
    return render(request, 'success.html')
