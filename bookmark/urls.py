# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.urls import path

from . import views

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/

from .api import BookmarkPostApi

#app_name = 'bookmark'
urlpatterns = [
    path('', views.index, name='bookmark-index'),
    path('list/', views.BookmarkListView.as_view(), name='bookmark-list'),
    #path('detail/<int:pk>/', views.BookmarkDetailView.as_view(), name='bookmark-detail'),
    path('create/', views.BookmarkCreateView.as_view(), name='bookmark-create'),
    path('update/<int:pk>/', views.BookmarkUpdateView.as_view(), name='bookmark-update'),
    path('delete/<int:pk>/', views.BookmarkDeleteView.as_view(), name='bookmark-delete'),
    path('api/', BookmarkPostApi.as_view(), name='bookmark-api'),
]
