from django.db import models
from datetime import date
# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    date = models.DateField()
    track = models.URLField()
    comments = models.TextField()

    @property
    def has_passed(self):
        return self.date < date.today()

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.name
