from django.http import Http404
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
import json
import httplib
import urllib

def make_request(query):
    tweet_strings = []
    iterations = 0
    print ":FJFJFJFJFJF"
    params = urllib.urlquote_plus({'?query':query, '?display':'json'})
    conn = httplib.HTTPConnection("geosparql.bbn.com")	    
    conn.request("POST", "/parliament/sparql", params)
    r1 = conn.getresponse()
    print r1.status, r1.reason

    if r1.status == 200: 
        response = r1.read()
    
 
	        
    conn.close
	
    return response

def get_triples(request):
    query = request.GET['query']
    request_strings = make_request(query)
    return HttpResponse(json.dumps(request_strings))


def get_coords(query):
    conn = httplib.HTTPConnection("geosparql.bbn.com")


def load_HTML(request):
    return render_to_response('ParlimentHTML.html')