# Generated by Django 4.1.3 on 2022-11-25 00:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Advert",
            fields=[
                (
                    "id_advert",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("advertising_platform", models.CharField(max_length=255)),
                ("platform_rate", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id_property",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("guest_limit", models.IntegerField()),
                ("bathrooms", models.IntegerField()),
                ("pets_accepted", models.BooleanField()),
                ("cleaning_cost", models.FloatField()),
                ("activation_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id_booking",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("check_in_date", models.DateField()),
                ("check_out_date", models.DateTimeField()),
                ("total_value", models.FloatField()),
                ("number_guests", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField()),
                (
                    "advert",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="properties.advert",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="advert",
            name="property",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="properties.property",
            ),
        ),
    ]
