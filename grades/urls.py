from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='grades-index'),
    path('create', views.create, name='grades-create'),
    path('update/<str:pk>/', views.update, name='grades-update'),
    path('delete/<str:pk>/', views.delete, name='grades-delete')
]