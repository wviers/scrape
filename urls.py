from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    (r'^tweets/(?P<twitter_name>\w+)/(?P<count>\d+)/$', 'tweet.views.tweet_view'),
    
    (r'^tweets/$', 'tweet.views.load_HTML'),
    
    (r'^tweets/(?P<query>\w+)/$', 'parliment.views.get_triples'),
    
    (r'^parliment/$', 'parliment.views.load_HTML'),
        
    # Examples:
    # url(r'^$', 'scrape.views.home', name='home'),
    # url(r'^scrape/', include('scrape.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),    
)
