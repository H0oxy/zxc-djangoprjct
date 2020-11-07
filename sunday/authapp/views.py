import django.contrib.auth as auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authapp.forms import LoginForm, RegisterForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    context = {
        'page_title': 'авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(reqest):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = RegisterForm

    context = {
        'page_title': 'Регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)