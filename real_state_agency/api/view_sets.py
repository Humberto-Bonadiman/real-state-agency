from rest_framework import viewsets
from real_state_agency.api import serializers
from properties import models


class PropertiesViewSet(viewsets.ModelViewSet):
    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertiesSerializer


""" class AdvertsViewSet(viewsets.ModelViewSet):
    queryset = models.Advert.objects.all()
    serializer_class = serializers.AdvertsSerializer """


""" class BookingsViewSet(viewsets.ModelViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingsSerializer """
