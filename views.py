
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from spotmyarena.forms import HomePageSearch

def indexView(request):
    if request.method == 'GET':
    	form = HomePageSearch()
    return render(request, "index.html", {'phoneNo' : '9876543210', 'form' : form, })
    return HttpResponse(html)

def searchResultsView(request):
    return render(request, "searchResults.html", {'phoneNo' : '9876543210'})
    return HttpResponse(html)

def clubProfile(request):
    return render(request, "clubProfile.html", {'phoneNo' : '9876543210'})
    return HttpResponse(html)

