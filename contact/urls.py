from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('free/', views.free_consult, name='free_consult'),
]
