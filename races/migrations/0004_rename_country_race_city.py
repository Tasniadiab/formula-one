# Generated by Django 4.2 on 2023-05-04 16:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("races", "0003_remove_race_has_passed"),
    ]

    operations = [
        migrations.RenameField(
            model_name="race",
            old_name="country",
            new_name="city",
        ),
    ]
