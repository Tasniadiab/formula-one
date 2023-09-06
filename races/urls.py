from django.urls import path
from races.views import race_list, race_detail

urlpatterns = [
    path("", race_list, name="race_list"),
    path("<int:id>/", race_detail, name="race_detail"),
]
