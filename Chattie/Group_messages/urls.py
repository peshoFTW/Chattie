from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_group, name='select_group'),
]
