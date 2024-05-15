from django.urls import path
from cart import views


app_name = 'cart'


urlpatterns = [
    path('', views.cart_page, name = 'cart'),
    path('add_item/', views.add_item, name = 'cart'),
]
