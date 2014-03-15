from django.shortcuts import render
from django.template import RequestContext
from datetime import datetime
from django.utils.dateformat import DateFormat

def context_rawBase(request):
    "A context processor that provides all variables used in the base html."
    return {
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
	'phoneNo' : '9876543210',
	'emailId' : 'spotmyarena@gmail.com',
	'todaysDate' : DateFormat(datetime.now()).format('d M Y'),
	
    }
