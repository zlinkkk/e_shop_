from django.db import models

# Create your models here.

class User(models.Model):
    login = models.EmailField(max_length=100, blank=False, null=False)
    # password = models.CharField(max_length=100, null=False, blank=False)
