from django.shortcuts import render

# Create your views here.


def catalog(request):
    return render(request, 'goods/catalog.html', {
        'products': [
            {
                'name': 'Вася пупин',
                'price': 'бесценно',
                'category': 'Категория 1'
                },
            {
                'name': 'Вася пупин',
                'price': 'бесценно',
                'category': 'Категория 1'
                },
            {
                'name': 'Вася пупин',
                'price': 'бесценно',
                'category': 'Категория 1'
                },
            {
                'name': 'Вася пупин',
                'price': 'бесценно',
                'category': 'Категория 1'
                },
        ]
    })


def product_page(request):
    return render(request, 'goods/product_page.html')