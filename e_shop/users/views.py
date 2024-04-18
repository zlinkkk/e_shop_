from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'users/login.html', {
        'title': 'Вход'
        })

def register(request):
    return render(request, 'users/register.html', {
        'title': 'Регистрация'
    })

def profile(request):
    return render(request, 'users/profile.html', {
        'title': 'Ваш профиль'
    })
