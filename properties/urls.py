from django.urls import path
from properties import views
from django.contrib import admin

urlpatterns = [
    path('property/<str:pk>/', views.property_detail),
    path('property/', views.property_list),
    path('advert/<str:pk>/', views.advert_detail),
    path('advert/', views.advert_list),
    path('booking/<str:pk>/', views.booking_detail),
    path('booking/', views.booking_list),
    path('admin/', admin.site.urls)
]
