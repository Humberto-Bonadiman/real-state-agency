from rest_framework import serializers
from properties.models import Property, Advert, Booking


class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id_booking',
            'check_in_date',
            'check_out_date',
            'total_value',
            'number_guests',
            'update_at',
            'created_at',
            'advert'
        ]


class AdvertsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advert
        fields = [
            'id_advert',
            'property',
            'advertising_platform',
            'platform_rate',
            'created_at',
            'update_at'
        ]


class PropertiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = [
            'id_property',
            'guest_limit',
            'bathrooms',
            'pets_accepted',
            'cleaning_cost',
            'activation_date',
            'comment_field',
            'created_at',
            'update_at'
        ]
