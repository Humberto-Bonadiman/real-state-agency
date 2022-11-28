# Generated by Django 4.1.3 on 2022-11-28 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("properties", "0003_alter_property_bathrooms_alter_property_guest_limit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advert",
            name="advertising_platform",
            field=models.CharField(default="advertising", max_length=255),
        ),
        migrations.AlterField(
            model_name="property",
            name="comment_field",
            field=models.CharField(default="comment", max_length=1000),
        ),
    ]
