from django.http import Http404
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
import json
import httplib


def make_request(query):
    conn = httplib.HTTPConnection("www.geosparql.bbn.com")
    request = []
	    

    conn.request("GET", "/parliament/sparql?query=" + query)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    
    if r1.status == 200:
        
        data1 = r1.read()
	try: 
       	    data2 = json.loads(data1)
    	    print ""
    	    print data2
	except:
	    return 'BROKEN' + data1
		
        while iterations < int(count):
            request.append(data2[iterations]['text'])
            iterations = iterations + 1
	        
		
    conn.close
	
    return request

def get_triples(request, query):
    request_strings = make_request(query)
    return HttpResponse(json.dumps(request_strings))



def load_HTML(request):
    return render_to_response('ParlimentHTML.html')