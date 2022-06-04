from django.contrib import admin
from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name="todolist-index"),
    #path('<str:slug>/', blog_post, name="blog-post"),
]