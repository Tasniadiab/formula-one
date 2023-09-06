from django.contrib import admin
from players.models import Players
# Register your models here.


@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):
    list_display = (
      "name",
      "country",
      "team",
    )
