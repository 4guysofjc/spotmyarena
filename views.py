
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.core import serializers
from spotmyarena.vendorData.models import Sport


def indexView(request):
    sport_list = serializers.serialize('python', Sport.objects.all(), fields=('sport_name'))
    return render(request, "index.html", {'phoneNo' : '9876543210', 'sport_list': sport_list, })
    return HttpResponse(html)

def searchResultsView(request):
    return render(request, "searchResults.html", {'phoneNo' : '9876543210'})
    return HttpResponse(html)

def clubProfile(request):
    return render(request, "clubProfile.html", {'phoneNo' : '9876543210'})
    return HttpResponse(html)

def all_json_areas(request, sport):
    current_sport = Sport.objects.get(sport_name=sport)
    areas = club.objects.all().filter(sport_id=current_sport)
    json_areas = serializers.serialize("json", areas)
    return HttpResponse(json_areas, mimetype="application/javascript")

