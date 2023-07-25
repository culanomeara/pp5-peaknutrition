from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    """
    Article model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article"
    )
    excerpt = models.TextField(blank=True)
    featured_image = models.ImageField(default='media/default.jpg')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
