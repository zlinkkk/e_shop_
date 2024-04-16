from django.contrib import admin

# Register your models here.
from django.contrib import admin

from . import models

# Register your models here.
@admin.register(models.PopularProducts)
class PopularProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )} 

   