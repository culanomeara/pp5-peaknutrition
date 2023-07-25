from django.db import models


class Category(models.Model):
    """
    Category Model for products
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Type(models.Model):
    """
    Type Model for products
    """
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Product Model
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    discount = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    featured_image = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.name
