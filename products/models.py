from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    discount = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    featured_image = models.ImageField(default='default.jpg')

    tags = TaggableManager()

    def __str__(self):
        return self.name
