

from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def indexView(request):
    return render(request, "index.html", {'phoneNo' : '9876543210'})
    return HttpResponse(html)


