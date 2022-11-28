from sqlite3 import IntegrityError
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from datetime import datetime

from properties.models import Property, Advert, Booking
from real_state_agency.api.serializers import (
  PropertiesSerializer,
  AdvertsSerializer,
  BookingsSerializer
)


@api_view(['GET', 'POST'])
def property_list(request):
    if request.method == 'GET':
        queryset = Property.objects.all()

        properties_serializer = PropertiesSerializer(queryset, many=True)
        return JsonResponse(properties_serializer.data, safe=False)

    elif request.method == 'POST':
        try:
            property_data = JSONParser().parse(request)
            first = second = third = 0
            first = property_data['guest_limit']
            second = property_data['bathrooms']
            third = property_data['cleaning_cost']

            if first < 0 or second < 0:
                raise IntegrityError
            property_serializer = PropertiesSerializer(data=property_data)

            if third < 0:
                return JsonResponse({
                    'message': '"cleaning_cost" cannot be less than 0'
                  },
                  status=status.HTTP_400_BAD_REQUEST)
            if property_serializer.is_valid():
                property_serializer.save()
                return JsonResponse(
                  property_serializer.data,
                  status=201
                )
            return JsonResponse(
              property_serializer.errors,
              status=400
            )
        except IntegrityError:
            return HttpResponse(status=400)


@api_view(['GET', 'PATCH', 'DELETE'])
def property_detail(request, pk):
    try:
        queryset = Property.objects.get(pk=pk)
    except Property.DoesNotExist or ValueError:
        return HttpResponse(status=404)

    if request.method == 'GET':
        property_serializer = PropertiesSerializer(queryset)
        return JsonResponse(property_serializer.data)

    elif request.method == 'PATCH':
        try:
            property_data = JSONParser().parse(request)
            first = second = third = 0
            first = property_data['guest_limit']
            second = property_data['bathrooms']
            third = property_data['cleaning_cost']

            if first < 0 or second < 0:
                raise IntegrityError
            if third < 0:
                return JsonResponse({
                    'message': '"cleaning_cost" cannot be less than 0'
                  },
                  status=status.HTTP_400_BAD_REQUEST)
            property_serializer = PropertiesSerializer(
              queryset,
              data=property_data,
              partial=True
            )
            if property_serializer.is_valid():
                property_serializer.save()
                return JsonResponse(
                  property_serializer.data,
                  status=201
                )
            return JsonResponse(
              property_serializer.errors,
              status=400
            )
        except IntegrityError:
            return HttpResponse(status=400)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status=204)


@api_view(['GET', 'POST'])
def advert_list(request):
    if request.method == 'GET':
        queryset = Advert.objects.all()

        advert_serializer = AdvertsSerializer(queryset, many=True)
        return JsonResponse(advert_serializer.data, safe=False)

    elif request.method == 'POST':
        advert_data = JSONParser().parse(request)
        advert_serializer = AdvertsSerializer(data=advert_data)
        platform_rate = advert_data['platform_rate']
        if platform_rate < 0:
            return JsonResponse({
                'message': '"platform_rate" cannot be less than 0'
                }, status=status.HTTP_400_BAD_REQUEST
            )
        if advert_serializer.is_valid():
            advert_serializer.save()
            return JsonResponse(
              advert_serializer.data,
              status=201
            )
        return JsonResponse(
          advert_serializer.errors,
          status=400
        )


@api_view(['GET', 'PATCH'])
def advert_detail(request, pk):
    try:
        queryset = Advert.objects.get(pk=pk)
    except Advert.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        advert_serializer = AdvertsSerializer(queryset)
        return JsonResponse(advert_serializer.data)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        advert_serializer = AdvertsSerializer(
          queryset,
          data=data,
          partial=True
        )
        platform_rate = data['platform_rate']
        if platform_rate < 0:
            return JsonResponse({
                'message': '"platform_rate" cannot be less than 0'
                }, status=status.HTTP_400_BAD_REQUEST
            )
        if advert_serializer.is_valid():
            advert_serializer.save()
            return JsonResponse(
              advert_serializer.data,
              status=201
            )
        return JsonResponse(
          advert_serializer.errors,
          status=400
        )


@api_view(['GET', 'POST'])
def booking_list(request):
    if request.method == 'GET':
        queryset = Booking.objects.all()

        bookings_serializer = BookingsSerializer(queryset, many=True)
        return JsonResponse(bookings_serializer.data, safe=False)

    elif request.method == 'POST':
        booking_data = JSONParser().parse(request)
        date_format = "%Y-%m-%d"
        message = '"check_in_date" or "check_out_date" is in wrong format'
        try:
            checkin = booking_data['check_in_date']
            checkin = datetime.strptime(checkin, date_format)
            checkout = booking_data['check_out_date'][:10]
            checkout = datetime.strptime(checkout, date_format)
            result = checkin < checkout

            booking_serializer = BookingsSerializer(data=booking_data)
            if result is False:
                return HttpResponse(status=400)
            if booking_serializer.is_valid():
                booking_serializer.save()
                return JsonResponse(
                  booking_serializer.data,
                  status=201
                )
        except ValueError:
            return JsonResponse(
              {
                'message': message,
                'check_in_date': 'YYYY-MM-DD format',
                'check_out_date': 'YYYY-MM-DDTHH:MM:SSZ format'
              },
              status=status.HTTP_400_BAD_REQUEST
            )


@api_view(['GET', 'DELETE'])
def booking_detail(request, pk):
    try:
        queryset = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        booking_serializer = BookingsSerializer(queryset)
        return JsonResponse(booking_serializer.data)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status=204)
