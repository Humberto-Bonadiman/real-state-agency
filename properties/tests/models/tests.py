from django.test import TestCase
from properties.models import Property, Advert, Booking
from datetime import date, datetime, timezone


out = datetime(2022, 10, 11, 10, 43, 55, 230, tzinfo=timezone.utc)


class PropertyTests(TestCase):
    def setUp(self):
        Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        Property.objects.create(
            guest_limit=3,
            bathrooms=1,
            pets_accepted=False,
            comment_field='Comentário',
            cleaning_cost=50.00,
            activation_date=date(2022, 6, 29)
        )

    def test_property(self):
        first_property = Property.objects.get(guest_limit=6)
        self.assertEqual(
            first_property.activation_date, date(2022, 5, 31)
        )
        self.assertEqual(
            first_property.pets_accepted, True
        )
        self.assertEqual(
            first_property.bathrooms, 2
        )
        self.assertEqual(
            first_property.comment_field, 'Comentário'
        )
        self.assertEqual(
            first_property.cleaning_cost, float(100)
        )
        self.assertEqual(
            first_property.guest_limit, 6
        )

        second_property = Property.objects.get(guest_limit=3)
        self.assertEqual(
            second_property.guest_limit, 3
        )
        self.assertEqual(
            second_property.bathrooms, 1
        )
        self.assertEqual(
            second_property.pets_accepted, False
        )
        self.assertEqual(
            second_property.comment_field, 'Comentário'
        )
        self.assertEqual(
            second_property.cleaning_cost, float(50)
        )
        self.assertEqual(
            second_property.activation_date, date(2022, 6, 29)
        )


class AdvertTest(TestCase):
    def setUp(self):
        Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        property_test = Property.objects.get(guest_limit=6)
        Advert.objects.create(
            advertising_platform='Airbnb',
            platform_rate=float(10.00),
            property=property_test
        )

    def test_advert(self):
        advert_test = Advert.objects.get(advertising_platform='Airbnb')
        self.assertEqual(
            advert_test.advertising_platform, 'Airbnb'
        )
        self.assertEqual(
            advert_test.platform_rate, float(10.00)
        )
        self.assertEqual(
            advert_test.property.guest_limit, 6
        )
        self.assertEqual(
            advert_test.property.bathrooms, 2
        )


class BookingTest(TestCase):
    def setUp(self):
        Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        property_test = Property.objects.get(guest_limit=6)
        Advert.objects.create(
            advertising_platform='Airbnb',
            platform_rate=float(10.00),
            property=property_test
        )
        advert_test = Advert.objects.get(advertising_platform='Airbnb')
        Booking.objects.create(
            check_in_date=date(2022, 10, 10),
            check_out_date=out,
            total_value=float(100.00),
            number_guests=1,
            advert=advert_test
        )

    def test_booking(self):
        booking_test = Booking.objects.get(check_in_date=date(2022, 10, 10))
        self.assertEqual(
            booking_test.check_in_date, date(2022, 10, 10)
        )
        self.assertEqual(
            booking_test.check_out_date,
            out
        )
        self.assertEqual(
            booking_test.total_value, float(100.00)
        )
        self.assertEqual(
            booking_test.number_guests, 1
        )
        self.assertEqual(
            booking_test.advert.advertising_platform, 'Airbnb'
        )
