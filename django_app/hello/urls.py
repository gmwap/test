from django.contrib import admin
from django.urls import path
from . import views
from .views import FriendList, FriendDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('find', views.find, name='find'),
    path('detail/<int:pk>', FriendDetail.as_view()),
    path('list', FriendList.as_view()),
]
