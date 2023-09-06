from django.contrib import admin
from teams.models import Teams

# Register your models here.


@admin.register(Teams)
class TeamsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "team_principle",
        "place_in_championship",
    )
