from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from users.forms import LoginForm

def login_page(request):
    # error_msg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['login'], password=data['password'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main:home'))
            
        # if not form.is_valid():
        #     error_msg = 'Введеный пользователь не существует.'
        
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {
        'title': 'Вход',
        'form': form,
        # 'error_msg': error_msg 
    })

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password2'])

            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('main:home'))

    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('profile:login'))

def profile(request):
    return render(request, 'users/profile.html', {
        'title': 'Ваш профиль'
    })

