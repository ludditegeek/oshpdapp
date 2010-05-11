# Note these URLS work in concert with the settings in mysite.urls.py
import os
from django.conf.urls.defaults import *
from oshpdapp.models import *
from oshpdapp.views import *
#

site_media = os.path.join(
                os.path.dirname(__file__), 'site_media'
                )


codelist_info = {
    'queryset': Codetbl.objects.all(),
    'template_name': 'codelist.html',
    #'template_object_name': 'codelist',
}

codetbl_info_dict = {
    'queryset': Codetbl.objects.all(),
}

ptmaster_info_dict = {
    'queryset': Ptmaster.objects.all(),
}

urlpatterns = patterns('',

# Browsing
  (r'^$', main_page),
  # After search link to dx list for patient
  # url(r'^search/dx/$', search_patient_dx, name='patient_search_dx'),
  
  url(r'^dxsearch/$', search_patient_dx, name='patient_search_dx'),
  # allow redirection with message passing (string passed in url)
  url(r'^dxsearch/.+$', search_patient_dx, name='patient_search_dx'),  
  url(r'^prsearch/$', search_patient_pr, name='patient_search_pr'),
  
  
  # After search link to prescreen list for patient  
  url(r'^search/pr/$', 'webapps.oshpdapp.views.search_patient_pr', name='patient_search_pr'),
  # After search link to abstraction list for patient  
  url(r'^search/ab/$', 'webapps.oshpdapp.views.search_patient_ab', name='patient_search_ab'),
  
# Patient Processing
# View generic patient list (need a template for this)
  #url(r'^ptmaster/$', 'django.views.generic.list_detail.object_list', ptmaster_info_dict, name='ptmaster_list'),
  #url(r'^edit/(?P<id>/d+)/$', 'mysite.oshpdcd.views.edit_patient', name='ptmaster_edit'),
  # prescreenselected patient
  url(r'^prescreen/$', 'webapps.oshpdapp.views.list_prescreen', name='ptmaster_list'),
  
  url(r'^prescreen/(\d+)$', edit_prescreen, name='prescreen_edit'),
  
  # patient ready for abstraction list (i.e. prescreen completed)
  url(r'^abstract/$', list_abstract),
  url(r'^abstract/(\d+)$', 'webapps.oshpdapp.views.edit_abstract', name='ptabstract_edit'),

  url(r'^edit/(\d+)$', 'webapps.oshpdapps.views.edit_ptmaster', name='ptmaster_edit'),

  # edit diagnosis codes
  url(r'^dx/(\d+)$', edit_dxcode, name='dxcode_edit'),
  # add diagnosis codes for selected patient
  url(r'^dxadd/(\d+)$', add_dxcode, name='dxcode_add'),
  
  # ptdetails maintenance
  # edit selected record
  url(r'^ptdtls/(\d+)$', edit_ptdetails, name='ptdtls_edit'),
  # add diagnosis code for selected patient
  url(r'^ptdtlsadd/(\d+)$', add_ptdetails, name='ptdtls_add'),
  
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     
     # test form
  url(r'^test/$', 'webapps.oshpdapps.views.test', name='ptabstract_list'),

    # Ajax request to lookup ICD9 codes
  url(r'^ajax/icd9/autocomplete/$', get_icd9_codes, name='icd9_lookup'),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    # add entry for generic list view
    # (r'^codelist/$', direct_to_template, {'template': 'codelist.html'}),
    #(r'^codelist/$', list_detail.object_list, codelist_info),
    # entry for detail view - pass id to detail form
    #(r'^codelist/(\d+)/$', cl_details),
     
)
