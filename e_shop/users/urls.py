from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_page, name = 'login'),
    path('logout/', views.logout_page, name = 'logout'),
    path('registration/', views.registration, name = 'register'),
    path('profile_page/', views.profile, name = 'user_page'),
]
