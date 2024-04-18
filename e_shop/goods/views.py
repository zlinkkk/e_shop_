from django.shortcuts import render
from goods.models import Products
from goods.utils import query_search

def catalog(request):
    query = request.GET.get('q', None)
    if query:
        goods = query_search(query)
    else:
        goods = Products.objects.all()

    return render(request, 'goods/catalog.html', {
        'title': 'Каталог',
        'goods': goods,
        'query': query,
        'count': len(goods)
    })


def product_page(request, search_slug):
    product = Products.objects.get(slug=search_slug)

    return render(request, 'goods/product_page.html',{
        'product': product
    })
