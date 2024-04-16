from django.db import models

# Create your models here.
class PopularProducts(models.Model):
    class Meta:
        db_table = 'popular_products'

    name = models.CharField(max_length = 100)
    price = models.FloatField(max_length = 100000)
    image = models.ImageField(upload_to='main_images')
    slug = models.SlugField(default = "", null = False)
    count = models.IntegerField(default=0, blank = False)