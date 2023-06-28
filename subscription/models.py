from django.db import models


class Subscription(models.Model):
    """
    Users can subscribe
    """
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
