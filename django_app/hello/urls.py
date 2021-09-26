from django.contrib import admin
from django.urls import path
from .views import HelloView, index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
