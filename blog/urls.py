# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.urls import path

from . import views

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/

from .api import BlogPostApi

#app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('list/', views.BlogListView.as_view(), name='blog-list'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('create/', views.BlogCreateView.as_view(), name='blog-create'),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='blog-update'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('api/', BlogPostApi.as_view(), name='blog-api'),
]
