from django.contrib import admin
from races.models import Race

# Register your models here.


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "date",
        "has_passed",
        "track",
        "results",
        "comments",
    )
