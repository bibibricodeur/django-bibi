# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.urls import path

from . import views

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/

from .api import WikiPostApi

#app_name = 'blog'
urlpatterns = [
    path('', views.index, name='wiki-index'),
    path('list/', views.WikiListView.as_view(), name='wiki-list'),
    path('detail/<int:pk>/', views.WikiDetailView.as_view(), name='wiki-detail'),
    path('api/',WikiPostApi.as_view(), name='wiki-api'),
]
