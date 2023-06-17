from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('<slug:slug>', views.article_detail, name='article_detail'),
]