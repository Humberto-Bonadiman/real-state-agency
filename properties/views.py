from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from properties.models import Property, Advert, Booking
from real_state_agency.api.serializers import (
  PropertiesSerializer,
  AdvertsSerializer,
  BookingsSerializer
)


@csrf_exempt
def property_list(request):
    if request.method == 'GET':
        queryset = Property.objects.all()

        properties_serializer = PropertiesSerializer(queryset, many=True)
        return JsonResponse(properties_serializer.data, safe=False)

    elif request.method == 'POST':
        property_data = JSONParser().parse(request)
        property_serializer = PropertiesSerializer(data=property_data)
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


@csrf_exempt
def property_detail(request, pk):
    try:
        queryset = Property.objects.get(pk=pk)
    except queryset.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        property_serializer = PropertiesSerializer(queryset)
        return JsonResponse(property_serializer.data)

    elif request.method == 'PATCH':
        property_data = JSONParser().parse(request)
        property_serializer = PropertiesSerializer(
          queryset,
          data=property_data,
          partial=True
        )
        if property_serializer.is_valid():
            property_serializer.save()
            return JsonResponse(
              property_serializer,
              status=201
            )
        return JsonResponse(
          property_serializer.errors,
          status=400
        )

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status=204)


@csrf_exempt
def advert_list(request):

    if request.method == 'GET':
        queryset = Advert.objects.all()

        advert_serializer = AdvertsSerializer(queryset, many=True)
        return JsonResponse(advert_serializer.data, safe=False)

    elif request.method == 'POST':
        advert_data = JSONParser().parse(request)
        advert_serializer = AdvertsSerializer(data=advert_data)
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


@csrf_exempt
def advert_detail(request, pk):
    try:
        queryset = Advert.objects.get(pk=pk)
    except queryset.DoesNotExist:
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


@csrf_exempt
def booking_list(request):
    if request.method == 'GET':
        queryset = Booking.objects.all()

        bookings_serializer = BookingsSerializer(queryset, many=True)
        return JsonResponse(bookings_serializer.data, safe=False)

    elif request.method == 'POST':
        booking_data = JSONParser().parse(request)
        booking_serializer = BookingsSerializer(data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse(
              booking_serializer.data,
              status=201
            )
        return JsonResponse(
          booking_serializer.errors,
          status=400
        )


@csrf_exempt
def booking_detail(request, pk):
    try:
        queryset = Booking.objects.get(pk=pk)
    except queryset.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        booking_serializer = BookingsSerializer(queryset)
        return JsonResponse(booking_serializer.data)

    elif request.method == 'DELETE':
        queryset.delete()
        return HttpResponse(status=204)
