from django.db import models
from uuid import uuid4


class Property(models.Model):
    id_property = models.UUIDField(
      primary_key=True, default=uuid4, editable=False)
    guest_limit = models.IntegerField()
    bathrooms = models.IntegerField()
    pets_accepted = models.BooleanField()
    cleaning_cost = models.FloatField()
    activation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()

    def __str__(self):
        return self.id_property


class Advert(models.Model):
    id_advert = models.UUIDField(
      primary_key=True, default=uuid4, editable=False)
    property = models.ForeignKey(
      Property, on_delete=models.SET_NULL, blank=True, null=True
    )
    advertising_platform = models.CharField(max_length=255)
    platform_rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()

    def __str__(self):
        return self.id_advert


class Booking(models.Model):
    id_booking = models.UUIDField(
      primary_key=True, default=uuid4, editable=False)
    advert = models.ForeignKey(
      Advert, on_delete=models.SET_NULL, blank=True, null=True
    )
    check_in_date = models.DateField()
    check_out_date = models.DateTimeField()
    total_value = models.FloatField()
    # comment_field = models.
    number_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField()

    def __str__(self):
        return self.id_booking
