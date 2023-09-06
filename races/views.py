from django.shortcuts import render, get_object_or_404
from races.models import Race

# Create your views here.
def race_list(request):
    all_races = Race.objects.all()
    context = {
        "all_races" : all_races,
    }
    return render(request, "races/races.html", context)

def race_detail(request, id):
    race_details = get_object_or_404(Race, id =id)
    context = {
        "race_details": race_details,
    }
    return render(request, "races/details.html", context)
