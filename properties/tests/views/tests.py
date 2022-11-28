import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from properties.models import Property, Advert, Booking
from real_state_agency.api import serializers
from datetime import date

client = Client()


class GetAllPropertiesTest(TestCase):
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

    def test_get_all_properties(self):
        response = client.get(reverse('property_list'), format='json')
        properties = Property.objects.all()
        serializer = serializers.PropertiesSerializer(properties, many=True)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePropertyTest(TestCase):
    def setUp(self):
        self.house = Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )

    def test_get_single_property(self):
        response = client.get(
            reverse('property_detail', kwargs={'pk': self.house.pk}))
        property = Property.objects.get(pk=self.house.pk)
        serializer = serializers.PropertiesSerializer(property)
        self.assertEqual(response.json(), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_property(self):
        response = client.get(
            reverse(
              'property_detail',
              kwargs={'pk': '1a2a3b3c-1211-2b2b-b3b4-1234567890ab'}
            ))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPropertyTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'guest_limit': 4,
            'bathrooms': 2,
            'pets_accepted': True,
            'cleaning_cost': 120.0,
            'activation_date': '2022-10-05',
            'comment_field': "comment",
        }
        self.invalid_payload = {
            'guest_limit': 4,
            'bathrooms': -2,
            'pets_accepted': True,
            'cleaning_cost': 120.0,
            'activation_date': '2022-10-05',
            'comment_field': "comment",
        }

    def test_create_valid_property(self):
        response = client.post(
            reverse('property_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_property(self):
        response = client.post(
            reverse('property_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSinglePropertyTest(TestCase):
    def setUp(self):
        self.first = Property.objects.create(
            guest_limit=4,
            bathrooms=2,
            pets_accepted=True,
            cleaning_cost=120.0,
            activation_date='2022-10-05',
            comment_field="comment",
        )

        self.valid_payload = {
            'guest_limit': 5,
            'bathrooms': 2,
            'pets_accepted': True,
            'cleaning_cost': 125.0,
            'activation_date': '2022-10-05',
            'comment_field': "comment",
        }
        self.invalid_payload = {
            'guest_limit': 4,
            'bathrooms': -2,
            'pets_accepted': True,
            'cleaning_cost': 120.0,
            'activation_date': '2022-10-05',
            'comment_field': "comment",
        }

    def test_valid_update_property(self):
        response = client.patch(
            reverse('property_detail', kwargs={'pk': self.first.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_update_property(self):
        response = client.patch(
            reverse('property_detail', kwargs={'pk': self.first.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePropertyTest(TestCase):
    def setUp(self):
        self.create = Property.objects.create(
            guest_limit=4,
            bathrooms=2,
            pets_accepted=True,
            cleaning_cost=120.0,
            activation_date='2022-10-05',
            comment_field="comment",
        )

    def test_valid_delete_property(self):
        response = client.delete(
            reverse('property_detail', kwargs={'pk': self.create.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_property(self):
        response = client.delete(
            reverse(
                'property_detail',
                kwargs={'pk': '1a2a3b3c-1211-2b2b-b3b4-1234567890ab'}
            ))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetAllAdvertsTest(TestCase):
    def setUp(self):
        property_created = Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        Advert.objects.create(
            property=property_created,
            advertising_platform="airbnb",
            platform_rate=12.0,
        )
        Advert.objects.create(
            property=property_created,
            advertising_platform="airbnb",
            platform_rate=10.0,
        )

    def test_get_all_advert(self):
        response = client.get(reverse('advert_list'), format='json')
        json_response = response.json()
        adverts = Advert.objects.all()
        serializer = serializers.AdvertsSerializer(adverts, many=True).data
        self.assertEqual(
            json_response[0]['id_advert'], serializer[0]['id_advert']
        )
        self.assertEqual(
            json_response[1]['id_advert'], serializer[1]['id_advert']
        )
        self.assertEqual(
            json_response[0]['advertising_platform'],
            serializer[0]['advertising_platform']
        )
        self.assertEqual(
            json_response[1]['advertising_platform'],
            serializer[1]['advertising_platform']
        )
        self.assertEqual(
            json_response[0]['platform_rate'], serializer[0]['platform_rate']
        )
        self.assertEqual(
            json_response[1]['platform_rate'], serializer[1]['platform_rate']
        )
        self.assertEqual(
            json_response[0]['created_at'], serializer[0]['created_at']
        )
        self.assertEqual(
            json_response[1]['created_at'], serializer[1]['created_at']
        )
        self.assertEqual(
            json_response[0]['update_at'], serializer[0]['update_at']
        )
        self.assertEqual(
            json_response[1]['update_at'], serializer[1]['update_at']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleAdvertTest(TestCase):
    def setUp(self):
        property_created = Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        self.house = Advert.objects.create(
            property=property_created,
            advertising_platform="airbnb",
            platform_rate=12.0,
        )

    def test_get_single_advert(self):
        response = client.get(
            reverse('advert_detail', kwargs={'pk': self.house.pk}))
        json_response = response.json()
        advert = Advert.objects.get(pk=self.house.pk)
        serializer = serializers.AdvertsSerializer(advert).data
        self.assertEqual(
            json_response['id_advert'], serializer['id_advert']
        )
        self.assertEqual(
            json_response['advertising_platform'],
            serializer['advertising_platform']
        )
        self.assertEqual(
            json_response['platform_rate'], serializer['platform_rate']
        )
        self.assertEqual(
            json_response['created_at'], serializer['created_at']
        )
        self.assertEqual(
            json_response['update_at'], serializer['update_at']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_advert(self):
        response = client.get(
            reverse(
              'advert_detail',
              kwargs={'pk': '1a2a3b3c-1211-2b2b-b3b4-1234567890ab'}
            ))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewAdvertTest(TestCase):
    def setUp(self):
        property_created = Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        self.valid_payload = {
            'property': str(property_created.id_property),
            'advertising_platform': 'airbnb',
            'platform_rate': 12.0,
        }
        self.invalid_payload = {
            'property': str(property_created.id_property),
            'advertising_platform': '',
            'platform_rate': 12.0,
        }

    def test_create_valid_advert(self):
        response = client.post(
            reverse('advert_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_advert(self):
        response = client.post(
            reverse('advert_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleAdvertTest(TestCase):
    def setUp(self):
        property_created = Property.objects.create(
            guest_limit=4,
            bathrooms=2,
            pets_accepted=True,
            cleaning_cost=120.0,
            activation_date='2022-10-05',
            comment_field="comment",
        )
        self.first = Advert.objects.create(
            property=property_created,
            advertising_platform='airbnb',
            platform_rate=12.0,
        )

        self.valid_payload = {
            'property': str(property_created.id_property),
            'advertising_platform': 'airbnb',
            'platform_rate': 10.0,
        }
        self.invalid_payload = {
            'property': str(property_created.id_property),
            'advertising_platform': 'platform',
            'platform_rate': -10.0,
        }

    def test_valid_update_advert(self):
        response = client.patch(
            reverse('advert_detail', kwargs={'pk': self.first.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_update_advert(self):
        response = client.patch(
            reverse('advert_detail', kwargs={'pk': self.first.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetAllBookingTest(TestCase):
    def setUp(self):
        property_created = Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        advert_created = Advert.objects.create(
            property=property_created,
            advertising_platform="airbnb",
            platform_rate=12.0,
        )
        Booking.objects.create(
            check_in_date="2022-11-10",
            check_out_date="2022-11-12T10:30:00Z",
            total_value=300.0,
            number_guests=1,
            advert=advert_created
        )
        Booking.objects.create(
            check_in_date="2022-11-15",
            check_out_date="2022-11-18T10:30:00Z",
            total_value=360.0,
            number_guests=1,
            advert=advert_created
        )

    def test_get_all_booking(self):
        response = client.get(reverse('booking_list'), format='json')
        json_response = response.json()
        booking = Booking.objects.all()
        serializer = serializers.BookingsSerializer(booking, many=True).data
        self.assertEqual(
            json_response[0]['id_booking'], serializer[0]['id_booking']
        )
        self.assertEqual(
            json_response[1]['id_booking'], serializer[1]['id_booking']
        )
        self.assertEqual(
            json_response[0]['check_in_date'],
            serializer[0]['check_in_date']
        )
        self.assertEqual(
            json_response[1]['check_in_date'],
            serializer[1]['check_in_date']
        )
        self.assertEqual(
            json_response[0]['check_out_date'], serializer[0]['check_out_date']
        )
        self.assertEqual(
            json_response[1]['check_out_date'], serializer[1]['check_out_date']
        )
        self.assertEqual(
            json_response[0]['total_value'], serializer[0]['total_value']
        )
        self.assertEqual(
            json_response[1]['total_value'], serializer[1]['total_value']
        )
        self.assertEqual(
            json_response[0]['number_guests'], serializer[0]['number_guests']
        )
        self.assertEqual(
            json_response[1]['number_guests'], serializer[1]['number_guests']
        )
        self.assertEqual(
            json_response[0]['created_at'], serializer[0]['created_at']
        )
        self.assertEqual(
            json_response[1]['created_at'], serializer[1]['created_at']
        )
        self.assertEqual(
            json_response[0]['update_at'], serializer[0]['update_at']
        )
        self.assertEqual(
            json_response[1]['update_at'], serializer[1]['update_at']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleBookingTest(TestCase):
    def setUp(self):
        property_created = Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        advert_created = Advert.objects.create(
            property=property_created,
            advertising_platform="airbnb",
            platform_rate=12.0,
        )
        self.house = Booking.objects.create(
            check_in_date="2022-11-15",
            check_out_date="2022-11-18T10:30:00Z",
            total_value=360.0,
            number_guests=1,
            advert=advert_created
        )

    def test_get_single_booking(self):
        response = client.get(
            reverse('booking_detail', kwargs={'pk': self.house.pk}))
        json_response = response.json()
        booking = Booking.objects.get(pk=self.house.pk)
        serializer = serializers.BookingsSerializer(booking).data
        self.assertEqual(
            json_response['id_booking'], serializer['id_booking']
        )
        self.assertEqual(
            json_response['check_in_date'],
            serializer['check_in_date']
        )
        self.assertEqual(
            json_response['check_out_date'], serializer['check_out_date']
        )
        self.assertEqual(
            json_response['total_value'], serializer['total_value']
        )
        self.assertEqual(
            json_response['number_guests'], serializer['number_guests']
        )
        self.assertEqual(
            json_response['created_at'], serializer['created_at']
        )
        self.assertEqual(
            json_response['update_at'], serializer['update_at']
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_booking(self):
        response = client.get(
            reverse(
              'booking_detail',
              kwargs={'pk': '1a2a3b3c-1211-2b2b-b3b4-1234567890ab'}
            ))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewBookingTest(TestCase):
    def setUp(self):
        property_created = Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        advert_created = Advert.objects.create(
            property=property_created,
            advertising_platform="airbnb",
            platform_rate=12.0,
        )
        self.house = Booking.objects.create(
            check_in_date="2022-11-15",
            check_out_date="2022-11-18T10:30:00Z",
            total_value=360.0,
            number_guests=1,
            advert=advert_created
        )
        self.valid_payload = {
            'check_in_date': '2022-11-15',
            'check_out_date': '2022-11-18T10:30:00Z',
            'total_value': 360.0,
            'number_guests': 1,
            'advert': str(advert_created.id_advert)
        }
        self.invalid_payload = {
            'check_in_date': '2022-11-20',
            'check_out_date': '2022-11-18T10:30:00Z',
            'total_value': 360.0,
            'number_guests': 1,
            'advert': str(advert_created.id_advert)
        }

    def test_create_valid_booking(self):
        response = client.post(
            reverse('booking_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_booking(self):
        response = client.post(
            reverse('booking_list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleBookingTest(TestCase):
    def setUp(self):
        property_created = Property.objects.create(
            guest_limit=6,
            bathrooms=2,
            pets_accepted=True,
            comment_field='Comentário',
            cleaning_cost=100.00,
            activation_date=date(2022, 5, 31)
        )
        advert_created = Advert.objects.create(
            property=property_created,
            advertising_platform="airbnb",
            platform_rate=12.0,
        )
        self.create = Booking.objects.create(
            check_in_date="2022-11-15",
            check_out_date="2022-11-18T10:30:00Z",
            total_value=360.0,
            number_guests=1,
            advert=advert_created
        )

    def test_valid_delete_booking(self):
        response = client.delete(
            reverse('booking_detail', kwargs={'pk': self.create.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_booking(self):
        response = client.delete(
            reverse(
                'booking_detail',
                kwargs={'pk': '1a2a3b3c-1211-2b2b-b3b4-1234567890ab'}
            ))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
