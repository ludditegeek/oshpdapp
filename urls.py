# Note these URLS work in concert with the settings in oshpdapp.urls.py and
# lgapp.urls.py 

import os.path
from django.conf.urls.defaults import *
#

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),
    
    # Include urls in app specific directory
    #(r'^oshpdcd/', include ('mysite.oshpdcd.urls')),
    # Site Media
  (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': 'site_media'}),
    
#    (r'^oshpdcd/', include ('mysite.oshpdcd.urls')),
#    )
    
  (r'^', include ('oshpdapp.urls')),
  (r'^', include ('lgapp.urls')),
  )
    
