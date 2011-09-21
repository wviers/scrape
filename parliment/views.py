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
    response = []
    params = urllib.urlencode({'query':query, 'output':'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"}
    conn = httplib.HTTPConnection("geosparql.bbn.com")
    conn.request("POST", "/parliament/sparql", params, headers)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    
    #if r1.status == 200: 
    #    response = r1.read()
	
	
    if r1.status == 200: 
        response = r1.read()
	try: 
	    data2 = json.loads(response)
	    print ""
	    print data2['results']['school']
	except:
	    return 'BROKEN DATA'
			
		        
		

	
	
	
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