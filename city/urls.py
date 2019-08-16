from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', city_list, name='city_list_url'),
    path('city/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('street/<int:pk>/', views.StreetDetailView.as_view(), name='street_detail'),
    path('city/create', CityCreate.as_view(), name='city_create_url'),
    path('city/new', StreetCreate.as_view(), name='street_create_url'),
]