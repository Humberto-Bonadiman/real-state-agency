from django.urls import path
from properties import views
from django.contrib import admin

urlpatterns = [
    path('property/<uuid:pk>/', views.property_detail, name='property_detail'),
    path('property/', views.property_list, name='property_list'),
    path('advert/<uuid:pk>/', views.advert_detail, name='advert_detail'),
    path('advert/', views.advert_list, name='advert_list'),
    path('booking/<uuid:pk>/', views.booking_detail, name='booking_detail'),
    path('booking/', views.booking_list, name='booking_list'),
    path('admin/', admin.site.urls)
]
