from django.urls import path
from . import views

urlPatterns = [
    path('', views.index, name="index"), 
    path('createTodo/', views.createTodo, name="createTodo"),
    path('deleteTodo/', views.deleteTodo, name="deleteTodo"),
    path('clearTodo/', views.clearTodo, name="clearTodo")
]