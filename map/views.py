from django.http import Http404
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
import json
import httplib
import urllib
from string import Template


def make_request(request):
    response = []
    return_list = []
    query = request.GET['query']

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
	except:
	    return 'BROKEN DATA'
    elif (r1.status == 400):
        return "400"
			

    conn.close

    items = len(data2['results']['bindings'])
    iterations = 0
    while (iterations < items):
        return_list.append(data2['results']['bindings'][iterations]['school_wkt']['value'])
        iterations = iterations + 1
    
    print return_list
    
    return HttpResponse(json.dumps(return_list))


def load_HTML(request):
    return render_to_response('mapHTML.html')
    
    
    
    
    