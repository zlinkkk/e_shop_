from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def cart_page(request):
    return render(request, 'cart/cart.html')

def add_item(request):
    return JsonResponse('Товар добавлен в корзину', safe=False)