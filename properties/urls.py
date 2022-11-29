from django.urls import path
from properties import views
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path(
        'api_schema/',
        get_schema_view(
            title='Real State Agency API',
            description='Guide for the REST API'
        ),
        name='api_schema'
    ),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
    path('property/<uuid:pk>/', views.property_detail, name='property_detail'),
    path('property/', views.property_list, name='property_list'),
    path('advert/<uuid:pk>/', views.advert_detail, name='advert_detail'),
    path('advert/', views.advert_list, name='advert_list'),
    path('booking/<uuid:pk>/', views.booking_detail, name='booking_detail'),
    path('booking/', views.booking_list, name='booking_list'),
    path('admin/', admin.site.urls)
]
