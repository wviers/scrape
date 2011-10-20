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

def make_request(query):
    response = []
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
	except:
	    return 'BROKEN DATA'
    elif (r1.status == 400):
        return "400"
			
    
    conn.close
	
    return data2['results']['bindings']

def get_triples(request):
    return_list = []
    query = request.GET['query']
    request_strings = make_request(query)
   
    items = len(request_strings)
    iterations = 0
    while (iterations < items):
        return_list.append(request_strings[iterations]['school']['value'])
        iterations = iterations + 1
    
    return HttpResponse(json.dumps(return_list))


def get_coords(request, num):
    response = []
    return_list = []
    
    query2 = Template("""
    		PREFIX geo: <http://www.opengis.net/ont/OGC-GeoSPARQL/1.0/> 
                PREFIX gn: <http://www.geonames.org/ontology#> 
                PREFIX gu: <http://cegis.usgs.gov/rdf/gu/featureID#> 
                PREFIX coor: <http://www.opengis.net/ont/OGC-GeoSPARQL/1.0/> 
                PREFIX geoname: <http://sws.geonames.org/>
                SELECT DISTINCT ?Coordinates WHERE { 
                GRAPH <http://example.org/data> 
                { 

                <http://sws.geonames.org/$number/>  geo:hasGeometry ?geo .
                ?geo coor:asWKT ?Coordinates .
                } 
                }""")    
  
    return_list = make_request(query2.substitute(number = num))
    if return_list == []:
        return HttpResponseNotFound("There is not a set of Coodinates for the requested Id.")
    
    return HttpResponse(json.dumps(return_list[0]['Coordinates']['value']))



def load_HTML(request):
    return render_to_response('ParlimentHTML.html')
    
    
    
    
    
