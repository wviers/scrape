
"""
USGS Rolla
Wayne Viers
"""
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


def make_request(request, TRLo, TRLa, BRLo, BRLa, BLLo, BLLa, TLLo, TLLa):
    """builds query, sends it, parses the response, and returns it.
    
    Recieves coordinates for a bounding rectangle, and builds those 
    coordiantes into a sparql query.  Next the funciton parses the JSON
    and returns the data as a JSON string.
    
    Arguments:
        TRLo: The top right longitude.
        TRLa: The top right latitude.
        BRLo: The bottom right longitude.
        BRLa: The bottom right latitude.
        BLLo: The bottom left longitude.
        BLLa: The bottom left latitude.
        TLLo: The top left longitude.
        TLLa: The top left latitude.
        
    Returns:
        A JSON string containing the queried information.
        
    Raises:
        None.
    """
    
    response = []
    return_list = []
    
    query = ('PREFIX geo: <http://www.opengis.net/ont/OGC-GeoSPARQL/1.0/> ' 
             'PREFIX geo-sf: <http://www.opengis.net/def/dataType/OGC-SF/1.0/> '
             'PREFIX gn: <http://www.geonames.org/ontology#> SELECT DISTINCT '
             '?school_name ?school_wkt WHERE { GRAPH <http://example.org/data> '
             '{ LET (?place := "POLYGON((' + TRLo + " " + TRLa + ', ' + BRLo 
             + " " + BRLa + ', ' + BLLo + " " + BLLa + ', ' + TLLo + " " + TLLa
             + ", " + TRLo + " " + TRLa +'))"^^geo-sf:WKTLiteral) . ?school a '
             'gn:Feature ; geo:hasGeometry ?school_geo ; gn:featureCode gn:S.SCH '
             '. ?atl_geo a geo:Geometry ; geo:asWKT ?place . ' 
             '?school_geo geo:sf-within ?atl_geo .  '
             '?school_geo geo:asWKT ?school_wkt . '
             '?school gn:name ?school_name. } }')

    print query
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
        return_list.append(data2['results']['bindings'][iterations]['school_name']['value'])
        iterations = iterations + 1
    
    print return_list    
    return HttpResponse(json.dumps(return_list))


def load_HTML(request):
    return render_to_response('mapUpdate.html')
    
    
    
    
    