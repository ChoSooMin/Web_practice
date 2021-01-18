from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # name은 줘도 되고 안줘도 된다
    path('createTodo/', views.createTodo, name="createTodo"), # createTodo로 들어온 것을 views.createTodo로 맵핑해준다
    path('deleteTodo/', views.deleteTodo, name="deleteTodo")
]