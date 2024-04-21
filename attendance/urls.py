from django.contrib import admin
from django.urls import path, include
from attendance import views

urlpatterns = [
    path('', views.index, name='attendance-index'),
    path('create', views.create, name='attendance-create'),
    path('update/<str:pk>', views.update, name='attendance-update'),
    path('delete/<str:pk>', views.delete, name='attendance-delete')
]