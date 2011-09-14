from django.http import Http404
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
import json
import httplib


def make_request(query):
    conn = httplib.HTTPConnection("geosparql.bbn.com")	    
    response = []
    conn.request("GET", "/parliament/sparql?query=" + query)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    request = r1
        		
    conn.close
	
    return response

def get_triples(request):
    query = request.GET['query']
    request_strings = make_request(query)
    return HttpResponse(json.dumps(request_strings))



def load_HTML(request):
    return render_to_response('ParlimentHTML.html')