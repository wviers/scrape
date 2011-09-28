from django.http import Http404
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse
import json
import httplib


def get_tweets(twitter_name, count):
    conn = httplib.HTTPConnection("www.twitter.com")
    tweet_strings = []
    iterations = 0
	    
    print "searching ", twitter_name
    print ""
    conn.request("GET", "/statuses/user_timeline.json?screen_name=" + twitter_name + "&count= " + count)
    r1 = conn.getresponse()
    print r1.status, r1.reason
    
    if r1.status == 200:
        if int(count) <= 20: 
            data1 = r1.read()
	    try: 
            	data2 = json.loads(data1)
    	    	print ""
	    except:
	    	return 'BROKEN DATA'
		
       	    while iterations < int(count):
                tweet_strings.append(data2[iterations]['text'])
	        iterations = iterations + 1
	        
		
    conn.close
	
    return tweet_strings

def tweet_view(request, twitter_name, count):
    if(int(count) > 20):
      return HttpResponse(status=403)
    tweet_strings = get_tweets(twitter_name, count)
    if(tweet_strings == []):
      return HttpResponse(status=404)
    return HttpResponse(json.dumps(tweet_strings))


def load_HTML(request):
    return render_to_response('TweetHTML.html')
    
    
    