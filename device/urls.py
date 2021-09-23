# https://docs.djangoproject.com/fr/3.1/intro/tutorial01/
from django.urls import path

from . import views

# https://docs.djangoproject.com/fr/3.1/intro/tutorial04/

from .api import DevicePostApi

#app_name = 'device'
urlpatterns = [
    path('', views.index, name='device-index'),
    path('list/', views.DeviceListView.as_view(), name='device-list'),
    path('detail/<int:pk>/', views.DeviceDetailView.as_view(), name='device-detail'),
    path('create/', views.DeviceCreateView.as_view(), name='device-create'),
    path('update<int:pk>/', views.DeviceDetailView.as_view(), name='device-update'),
    path('delete<int:pk>/', views.DeviceDeleteView.as_view(), name='device-delete'),
    path('api/',DevicePostApi.as_view(), name='device-api'),
]
