from django.contrib.auth.models import AbstractUser
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25,blank=True)
    slug = models.CharField(max_length=30,blank=True,default=None)
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=200,blank=True)
    price = models.IntegerField(blank=True)
    description = models.CharField(max_length=500000,blank=True)
    cat = models.ForeignKey("Category",models.PROTECT,default=None)
    tag = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
class ProductImage_Filter(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    cover = models.BooleanField(blank=True,default=False)

    def __str__(self):
        return f"Image for {self.product.name}"


class User(AbstractUser):
    name = models.CharField(max_length=200,blank=True)
    fullname = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

