from django.shortcuts import render
from main.models import PopularProducts

def home(request):
    objects = PopularProducts.objects.all()
    return render(request, 'main/home.html', 
        {'title': 'Главная',
         'goods': objects})