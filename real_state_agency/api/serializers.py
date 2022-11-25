from rest_framework import serializers
from properties.models import Property


""" class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__' """


""" class AdvertsSerializer(serializers.ModelSerializer):
    bookings = BookingsSerializer(many=True)

    class Meta:
        model = Advert
        fields = (
            'id_advert',
            'advertising_platform',
            'platform_rate',
            'created_at',
            'update_at',
            'bookings'
        ) """


class PropertiesSerializer(serializers.ModelSerializer):
    # adverts = AdvertsSerializer(many=True)

    class Meta:
        model = Property
        fields = (
            'id_property',
            'guest_limit',
            'bathrooms',
            'pets_accepted',
            'cleaning_cost',
            'activation_date',
            'update_at',
            # 'adverts'
        )
