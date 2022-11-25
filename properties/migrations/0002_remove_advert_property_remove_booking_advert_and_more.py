# Generated by Django 4.1.3 on 2022-11-25 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="advert", name="property",),
        migrations.RemoveField(model_name="booking", name="advert",),
        migrations.AddField(
            model_name="advert",
            name="bookings",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="properties.booking",
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="adverts",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="properties.advert",
            ),
        ),
    ]
