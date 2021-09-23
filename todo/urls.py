# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.urls import path

from . import views

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/

#app_name = 'todo'
urlpatterns = [
    path('', views.index, name='todo-index'),
    path('list/', views.TodoListView.as_view(), name='todo-list'),
    path('detail/<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
    path('create/', views.TodoCreateView.as_view(), name='todo-create'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='todo-update'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='todo-delete'),
]
