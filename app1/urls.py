from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('profil/', views.profil),
    path('data/', views.data),
]
