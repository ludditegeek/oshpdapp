from django.conf.urls.defaults import *
#from demo.views import hello, current_datetime, hours_ahead,test, homepage, devtoolbag, lgabout
from lgapp.views import *
from django.conf import settings
import os


urlpatterns = patterns('',
    # Example:
    # (r'^ludditegeek/', include('testsite.foo.urls')),
    # Replaced above version with more generic version
    # 4/23/2009 - how to define this to avoid repitition of names/defs
     #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'D:/_DjangoApps/ludditegeek/media/'}),
     #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'MEDIA_ROOT'}),
     #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}) ,              
     (r'^$', gaebrowser),
     (r'^homepage/$', gaebrowser),
     (r'^devtoolbag/$', devtoolbag),
     (r'^lgabout/$', lgabout),
     (r'^cruddemo/$', cruddemo),
     (r'^gaebrowser/$', gaebrowser),
     (r'^menutree/$', menutree),
     (r'^datagrid/$', datagrid),
     (r'^howtosyntax/$', howtosyntax),
     (r'^howtofooter/$', howtofooter),
     (r'^admin/', include('django.contrib.admin.urls')),
     #(r'^', include('ludditegeek.web.urls')),     
     #(r'^test/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'images'}),
     #(r'^.?/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'images'}),
     #(r'^devtoolbag/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'images'}),
     #(r'^homepage/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'images'}),
                       
)
if settings.DEBUG:
    urlpatterns += patterns('',
        #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'D:/_DjangoApps/ludditegeek/media/'}),
        #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'D:/_DjangoApps/ludditegeek/'}),
        #(r'^homepage/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
                                                           #'D:/_DjangoApps/ludditegeek/media/'}),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':
                                                           'D:/_DjangoApps/ludditegeek/media/'}),
        #(r'%s(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), "site_media")}),
    )

