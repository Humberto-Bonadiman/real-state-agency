from rest_framework import serializers
from properties.models import Property, Advert, Booking


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class AdvertsSerializer(serializers.ModelSerializer):
    advert_bookings = BookingsSerializer(many=True)

    class Meta:
        model = Advert
        fields = '__all__'


class PropertiesSerializer(serializers.ModelSerializer):
    post_adverts = AdvertsSerializer(many=True)

    class Meta:
        model = Property
        fields = '__all__'
