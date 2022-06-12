from django.contrib import admin
from django.urls import path

from .views import index, lists

urlpatterns = [
    path('', index, name="todolist-index"),
    path('lists/', lists, name="todolist-lists"),
]
