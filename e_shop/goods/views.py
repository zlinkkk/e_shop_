from django.shortcuts import render

from goods.models import Products


def catalog(request):
    goods = Products.objects.all()
    return render(request, 'goods/catalog.html', {
        'title': 'Каталог',
        'goods': goods
    })


def product_page(request, search_slug):
    product = Products.objects.get(slug=search_slug)

    return render(request, 'goods/product_page.html',{
        'product': product
    })