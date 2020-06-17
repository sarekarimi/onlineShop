from django.db import models


# Create your models here.
class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    parent_id = models.IntegerField()
    rootIndex = models.IntegerField()
    discription = models.TextField()


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    sku = models.CharField(max_length=30)
    title_main = models.CharField(max_length=100)
    title_sub = models.CharField(max_length=100)
    price = models.IntegerField()
    brand_id = models.ForeignKey(Brand, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created = models.DateTimeField()
    updated = models.DateTimeField()
