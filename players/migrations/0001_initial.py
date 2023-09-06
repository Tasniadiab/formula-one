# Generated by Django 4.2 on 2023-05-03 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("teams", "0001_initial"),
        ("races", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Players",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("country", models.CharField(max_length=250)),
                (
                    "races",
                    models.ManyToManyField(related_name="results", to="races.race"),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="players_team",
                        to="teams.teams",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]