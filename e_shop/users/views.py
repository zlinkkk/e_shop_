from django.shortcuts import render
from users.forms import LoginForm

# Create your views here.
def login(request):
    form = LoginForm()
    return render(request, 'users/login.html', {
        'title': 'Вход',
        'form': form
        })

def register(request):
    return render(request, 'users/register.html', {
        'title': 'Регистрация'
    })

def profile(request):
    return render(request, 'users/profile.html', {
        'title': 'Ваш профиль'
    })
