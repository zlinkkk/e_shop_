from django.db import models

class Products(models.Model):
    class Meta:
        db_table = 'products'

    name = models.CharField(max_length = 100, null = False)
    color = models.CharField(max_length = 30)
    price = models.FloatField(max_length = 100000, null = False)
    description = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='goods_images')
    slug = models.SlugField(default = "", null = False)
    count = models.IntegerField(default=0)
    