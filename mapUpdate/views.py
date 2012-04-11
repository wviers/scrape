
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


def make_update(request, featureName, lon, lat):
    response = []
    return_list = []
    graph = urllib.quote('http://waynetest.example.org/')
	
    index = get_index()
    index = str(index)
 
    query = ('PREFIX gn: <http://www.geonames.org/ontology#>  '
		'PREFIX geo: <http://www.opengis.net/def/geosparql/> '
		'INSERT DATA { ' 
        'GRAPH <http://waynetest.example.org/> { '
		'<http://waynetest.example.org/#' + index + '> gn:name ' +  '"' + featureName + '"' + '. '  
		'<http://waynetest.example.org/#' + index + 'geo/> a geo:Geometry. '
		'<http://waynetest.example.org/#' + index + '> geo:hasGeometry <http://waynetest.example.org/#' + index + 'geo/>. '
		'<http://waynetest.example.org/#' + index + 'geo/> geo:asWKT "POINT( ' + lon + ' ' + lat + ' )". '
		'} } ')

	
    params = urllib.urlencode({'update':query, 'output':'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"}
    conn = httplib.HTTPConnection("usgs-ybother.srv.mst.edu:8890")
    conn.request("POST", "/parliament/sparql?graph=" + graph, params, headers)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    print r1.read()

    if r1.status == 200: 
        response = r1.read()

    conn.close

    return response

	
def get_index():
    response = []
    return_list = []
    index = ''
    graph = urllib.quote('http://waynetest.example.org/')

    query = ('PREFIX gn: <http://www.geonames.org/ontology#>'
        'SELECT DISTINCT ?item WHERE { GRAPH <http://waynetest.example.org/> {'
        '?item gn:name ?name. }}')

    params = urllib.urlencode({'query':query, 'output':'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"}
    conn = httplib.HTTPConnection("usgs-ybother.srv.mst.edu:8890")
    conn.request("POST", "/parliament/sparql?graph=" + graph, params, headers)
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

    if len(data2['results']['bindings']) == 0:
        index = '0'
    else:
        characters = list(data2['results']['bindings'][0]['item']['value'])
        start = data2['results']['bindings'][0]['item']['value'].index('#') + 1
        while start < len(characters):
            index = index + characters[start]
            start = start + 1
	
    index = int(index) + 1
    return index
	

def load_HTML(request):
    return render_to_response('mapUpdate.html')
    
    
    
    
    