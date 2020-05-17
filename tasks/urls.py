
from django.urls import path, include
from .views import home, TodoDetail, CreateTodo, UpdateTodo, DeleteTodo

urlpatterns = [
    path('', home, name='home'),
    path('todo/<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('create-todo/', CreateTodo.as_view(), name='create'),
    path('todo/<int:pk>/update/', UpdateTodo.as_view(), name='updateview'),
    path('todo/<int:pk>/delete/', DeleteTodo.as_view(), name='delete'),
    
]



