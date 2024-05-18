from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name')} 
