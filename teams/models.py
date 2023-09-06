from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    team_principle = models.CharField(max_length=250)
    place_in_championship = models.SmallIntegerField(null = True, blank = True)

    def __str__(self):
        return self.name
