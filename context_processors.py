from django.shortcuts import render
from django.template import RequestContext

def context_rawBase(request):
    "A context processor that provides all variables used in the base html."
    return {
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR'],
	'phoneNo' : '9876543210',
	'emailId' : 'spotmyarena@gmail.com',
	
    }
