from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace = 'main')),
    path('catalog/', include('goods.urls', namespace = 'catalog')),
    path('profile/', include('users.urls', namespace = 'profile')),
    path('cart/', include('cart.urls', namespace='cart'))
]

# debug on only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
