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
    iterations = 0
    return_list = []
    
    params = urllib.urlencode({'query':query, 'output':'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"}
    conn = httplib.HTTPConnection("geosparql.bbn.com")
    conn.request("POST", "/parliament/sparql", params, headers)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    
	
	
    if r1.status == 200: 
        response = r1.read()
	try: 
	    data2 = json.loads(response)
	    print ""
	    print "ELEMENT"
	    items = len(data2['results']['bindings'])
	    print items
	    print ""
	except:
	    return 'BROKEN DATA'
			
		        
		
    while (iterations < items):
        print data2['results']['bindings'][iterations]['school']['value']
        return_list.append(data2['results']['bindings'][iterations]['school']['value'])
        iterations = iterations + 1
	
	
	
    conn.close
	
    return return_list

def get_triples(request):
    query = request.GET['query']
    request_strings = make_request(query)
    return HttpResponse(json.dumps(request_strings))


def get_coords(query):
    conn = httplib.HTTPConnection("geosparql.bbn.com")


def load_HTML(request):
    return render_to_response('ParlimentHTML.html')