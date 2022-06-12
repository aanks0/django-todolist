from django.contrib import admin
from django.urls import path

from .views import index, lists, list_edit

urlpatterns = [
    path('', index, name="todolist-index"),
    path('lists/', lists, name="todolist-lists"),
    path('lists/<str:slug>/', list_edit, name="todolist-list-edit")
]
