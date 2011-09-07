from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^tweet/', include('tweet.urls')),
    (r'^admin/', include(admin.site.urls)),
)