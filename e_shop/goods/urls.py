from django.urls import path

from goods import views


app_name = 'main'

urlpatterns = [
    path('', views.catalog),
    path('product/', views.product_page)
]