from django.urls import path

from goods import views


app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name = 'index'),
    path('search/', views.catalog, name = 'search'),
    path('product/<str:search_slug>/', views.product_page, name = 'product')
]