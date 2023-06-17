from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles.as_view(), name='articles'),
    # path('<slug:slug>', views.article_detail, name='article_detail'),
]
