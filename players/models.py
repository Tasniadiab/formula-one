from django.db import models
from teams.models import Teams
from races.models import Race

# Create your models here.

class Players(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    team = models.ForeignKey(
        Teams,
        related_name = "players_team",
        on_delete = models.CASCADE
    )
    races = models.ManyToManyField(
        Race,
        related_name= "results",
        )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
