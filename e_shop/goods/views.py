from django.shortcuts import render

# Create your views here.


def catalog(request):
    return render(request, 'goods/catalog.html')


def product_page(request):
    return render(request, 'goods/product_page.html')