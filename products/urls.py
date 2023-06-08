from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('special_offers/', views.special_offers, name='special_offers'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
