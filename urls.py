from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^tweets/(?P<twitter_name>\w+)/(?P<count>\d+)/$', 'tweet.views.tweet_view'),
    
    (r'^tweets/$', 'tweet.views.load_HTML'),
    
    (r'^parliment/sparql/$', 'parliment.views.get_triples'),
    
    (r'^parliment/coords/(?P<num>\w+)/$', 'parliment.views.get_coords'),
    
    (r'^parliment/$', 'parliment.views.load_HTML'),
    
    (r'^map/sparql/(?P<TRLo>-?\d+\.\d{4})/(?P<TRLa>-?\d+\.\d{4})/(?P<BRLo>-?\d+\.\d{4})/(?P<BRLa>-?\d+\.\d{4})/(?P<BLLo>-?\d+\.\d{4})/(?P<BLLa>-?\d+\.\d{4})/(?P<TLLo>-?\d+\.\d{4})/(?P<TLLa>-?\d+\.\d{4})/$', 'map.views.make_request'),
    
    (r'^map/$', 'map.views.load_HTML'),
        
    (r'^rdfTest/$', 'rdfTest.views.load_HTML'),
    
    (r'^rdfTest/query/$', 'rdfTest.views.make_request'),
    
    (r'^rdfTest/jquery.rdfquery.rules.min-1.0/$', 'rdfTest.views.make_request'),
	
	(r'^sparqleUpdate/$', 'sparqleUpdate.views.load_HTML'),
	
	(r'^sparqleUpdate/sparql/$', 'sparqleUpdate.views.make_update'),
	
    (r'^mapUpdate/$', 'mapUpdate.views.load_HTML'),
	
	(r'^mapUpdate/sparql/(?P<featureName>\w+)/(?P<lon>-?\d+\.\d{4})/(?P<lat>-?\d+\.\d{4})/$', 'mapUpdate.views.make_update'),
)
