# Generated by Django 4.2 on 2023-05-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teams",
            name="place_in_championship",
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
