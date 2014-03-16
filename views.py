
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.core import serializers
from spotmyarena.vendorData.models import Sport,Club
from spotmyarena.context_processors import context_rawBase
from django.template import RequestContext
from urlparse import urlparse, parse_qs
from django.shortcuts import render_to_response

def indexView(request):
	sport_list = serializers.serialize('python', Sport.objects.all(), fields=('sport_name','sport_id'))
	return render(request, "index.html", { 'sport_list': sport_list, }, 
		context_instance=RequestContext(request, processors=[context_rawBase]))
	return HttpResponse(html)
		

def searchResultsView(request):
	query_dict = parse_qs(request.GET.urlencode())
	selected_sport_id = query_dict['sport_name'][0]
	selected_area = query_dict['sport_area'][0]
	selected_date = query_dict['sport_date'][0]
	club_list = serializers.serialize('python', 
		Club.objects.all().filter(club_area = selected_area, club_sport_id = selected_sport_id), 
		fields=('club_name','club_address','club_area','club_city','club_pincode'))
    	return render(request, "searchResults.html", { 'club_list': club_list, },
		context_instance=RequestContext(request, processors=[context_rawBase]))
    	return HttpResponse(html)
	    
def clubProfile(request):
	return render(request, "clubProfile.html", context_instance=RequestContext(request, processors=[context_rawBase]))
	return HttpResponse(html)

def all_json_areas(request, sportId):
	current_sport = Sport.objects.get(sport_id=sportId)
	areas = Club.objects.all().filter(club_sport_id=current_sport)
	json_areas = serializers.serialize("json", areas)
	return HttpResponse(json_areas, mimetype="application/javascript")

