from django.shortcuts import render
from django.http import JsonResponse
from goods.models import *
from .models import *
import json


# Create your views here.
def cart_page(request):
    return render(request, 'cart/cart.html')

def add_item(request):
    data = json.loads(request.body)
    product_id = data['product_id']
    action = data['action']
    print(action, product_id)


    return JsonResponse('Товар добавлен в корзину', safe=False)
