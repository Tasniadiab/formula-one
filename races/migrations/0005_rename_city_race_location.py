# Generated by Django 4.2 on 2023-05-04 16:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("races", "0004_rename_country_race_city"),
    ]

    operations = [
        migrations.RenameField(
            model_name="race",
            old_name="city",
            new_name="location",
        ),
    ]
