
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

def make_update(request):
    response = []
    return_list = []
    graph = urllib.quote('http://waynetest.example.org/')

    query = ("""
		PREFIX gn: <http://www.geonames.org/ontology#> 
		INSERT DATA { 
         GRAPH <http://waynetest.example.org/> { 
		 <http://waynetest.example.org/var3> gn:name "TEST". } } 
			""")

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



def load_HTML(request):
    return render_to_response('UpdateHTML.html')
    
    
    
    
    
