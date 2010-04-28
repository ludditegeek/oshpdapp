# Create your views here.
# ?? How to break these out into > 1 file ??

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse

# Parse URL - will extract PID 
import urlparse

# Not avail in v1.1
#from django.contrib import messages

from oshpdapp.forms import *
from oshpdapp.models import *
from oshpdapp.myforms import *

# Utility method to manage redirection - uses hidden form field to save value for next
def _get_next(request):
    """
    1. If there is a variable named ``next`` in the *POST* parameters, the view will
    redirect to that variable's value.
    2. If there is a variable named ``next`` in the *GET* parameters, the view will
    redirect to that variable's value.
    3. If Django can determine the previous page from the HTTP headers, the view will
    redirect to that previous page.
    """
    return request.POST.get('next', request.GET.get('next', request.META.get('HTTP_REFERER', None)))

def main_page(request):
  return render_to_response(
    'main_page.html',
    RequestContext(request)
  )

def success(request):
    # target page after successful update    
    return render_to_response('success.html')
    
def edit_prescreen(request, patient_id):
    # retrieve and edit patient 
    
    ent = get_object_or_404(Ptmaster, pk = patient_id)
    if request.method == 'GET':
        #create a form to add a new record  
        message = 'edit prescreen entry' 
        form =  PrescreenForm()                   
     
    if request.method == 'POST':       
        #create and populate a form    
        form =  PrescreenForm( data=request.POST, instance=ent)
        # How to check for checkbox style fields - check if in request[params]
        srcp = False
         
        if form.is_valid():
            p = form.save(commit=False)
            # Set default value
            p.absstatus = 'PENDING'
            # Enable Abstatus if SSN and DOB are correct
            #if (request.POST['ssncrct'] =='YES' and request.POST['bthdatecrct'] == 'YES'):
            if (form.cleaned_data['ssncrct'] =='YES' and form.cleaned_data['bthdatecrct'] == 'YES'):
                p.absstatus = 'PRESCREENOK'                
            p.save()
            # this is confusing - when to use reverse?
            # create confirmation message
            #next = _get_next(request)
            
            #messages.add_message(request, messages.INFO, 'Prescreen record updated for Patient %s.' %patient_id)
            return HttpResponseRedirect('/search') 
                      
    else:
        form = PrescreenForm(instance=ent)                        
        #form = PatientForm(edit_patient.html, { 'form': form}  )                        
    return render_to_response('prescreen_custom_form.html',
                                 {'form':form, 'add':False})
                                                                                                   
def list_prescreen(request):
    # list all pts pending prescreen
    error = False
    form = SearchForm()
    patients = []
    show_results = False
    #    patients = Ptmaster.objects.exclude(absstatus__isnull='PRESCREENOK')
    patients = Ptmaster.objects.exclude(absstatus__isnull=False)
    #patients = Ptmaster.objects.all()
    
            
    variables = RequestContext(request, {
    'form': form,
    'patients': patients,
    'show_results': True,
    'show_tags': True,
    'show_user': True,
    'error': error
    })
    if request.GET.has_key('ajax'):
        return render_to_response('prescreen_pending.html', variables)
    else:
        return render_to_response('prescreen_pending.html', variables)
                    
        
def edit_abstract(request, patient_id):
    # retrieve and edit patient 
    
    ent = get_object_or_404(Ptmaster, pk = patient_id)
    if request.method == 'GET':
        #create a form to edit a record  
        message = 'edit patient abstraction entry' 
        form =  AbstractionForm()                   
     
    if request.method == 'POST':       
        #create and populate a form    
        form =  AbstractionForm( data=request.POST, instance=ent)                  
        if form.is_valid():
            # ?? Use RE Validation on zip code; MRN ?? 
            p = form.save(commit=False)
            p.save()
            return HttpResponseRedirect('/search') 
                      
    else:
        form = AbstractionForm(instance=ent)                        
    return render_to_response('abstraction_form.html',
                                 {'form':form, 'add':False})   
                                 
                                 
def edit_dxcode(request, code_id):
    # edit diagnosis code

    #ent = get_object_or_404(Ptdx, pk = int(code_id)
    ent = get_object_or_404(Ptdx, id = code_id)
    
    #ent = get_object_or_404(Ptdx, pk = 1)
    
    #assert False
    
    if request.method == 'GET':
        #create a form to edit a record
        message = 'edit diagnosis code' 
        form =  DxForm()                   
     
    if request.method == 'POST':       
        #create and populate a form    
        form =  DxForm( data=request.POST, instance=ent)                  
        if form.is_valid():
            # ?? Use RE Validation on zip code; MRN ?? 
            p = form.save(commit=False)
            p.save()
            return HttpResponseRedirect('/search')                       
    else:
        form = DxForm(instance=ent)  
        #form = DxForm()  
                              
    return render_to_response('dx_form.html',
                                 {'form':form, 'add':False})   
                                 
                                 
def add_dxcode(request, patient_id):
    # Add new Code rec for selected patient
    pass                                 
         
                  
def edit_ptdetails(request, id):

    #ent = get_object_or_404(Ptdetails, id = 1)
    # find selected 
    #assert False
    ent = get_object_or_404(Ptdx, id = id)

    # edit selected ptdtls rec
    if request.method == 'GET':
        #create a form to edit a record  
        message = 'edit details code'
        #assert False
        form =  DtlsForm()                   
        # replace with CstmDtlsForm (4/20/10 - Not Required - Confirm)
        #form =  CstmDtlsForm()                   
     
    if request.method == 'POST':       
        #create and populate a form    
        form =  DtlsForm( data=request.POST, instance=ent)                  
        #form =  CstmDtlsForm( data=request.POST, instance=ent)                  
        if form.is_valid():
            # ?? Use RE Validation on zip code; MRN ?? 
            p = form.save(commit=False)
            p.save()
            # on redirect need to pass confirmation message
            # msg = 'Record Successfully Updated' - (redirect to previous screen?)
            # ?? render_to_response vs redirect ??
	    
	    # extract id value from url
	    #id = urlparse.urlparse(request.url).path.split('/')[-1]
	    
	    pl = urlparse.urlparse(request.META.get('HTTP_REFERER', None)).path.split('/')[-1]
	    
	    #url = request.META.get('HTTP_REFERER', None)
	    #pl = urlparse.urlparse(url)
	    #id = pl.path.split('/')[-1]
	    
            #msg_confirm = 'Dtls Entry %s successfully updated' %request.POST['id'] 
            #msg_confirm = 'Diagnosis Details Entry %s successfully updated' %id 
            
            # Create a session entry for this
            request.session['confirm'] = 'Dx Details Update for record #%s Successful' %pl
                        
            # use urlparse to access the id key (or get via a hidden field)                       
            #return HttpResponseRedirect('/dxsearch/' + msg_confirm)        
            return HttpResponseRedirect('/dxsearch' )        
                           
    else:
        #form = CstmDtlsForm(instance=ent)  
        form = DtlsForm(instance=ent)  
                             
    #return render_to_response('ptdetails_form.html',
    #                             {'form':form, 'add':False})   
    return render_to_response('dx_custom_form.html',
                                 {'form':form, 'add':True}) 
                                              
                                                   
def add_ptdetails(request, pid):

# Create new details entry for the currently selected patient id
# ?? Pass this as the a session object, rather than via url parm

    if request.method == 'POST':       
        #create and populate a form    
#        form =  DtlsForm( data=request.POST, instance=ent)    
        form =  DtlsForm( data=request.POST)    
        #form =  CstmDtlsForm( data=request.POST)    
                      
        if form.is_valid():
            # Create new PtDx entry 
            # Init with parent patient id etc.
            # 
            
            new_dtls = form.save(commit= False)
            new_dtls.ptmaster_id = pid
            new_dtls.save()
#            p = form.save(commit=False)
#            p.save()
#            return HttpResponseRedirect('/search') 
#            return HttpResponseRedirect(new_dtls.get_absolute_url()) 
            # ?? Where to go after save ??
#            return HttpResponseRedirect(new_dtls.get_absolute_url()) 

            # save and return to calling screen
            return HttpResponseRedirect('/dxsearch') 
                                             
    else:
        # Form has errors 
        form = DtlsForm(data=request.POST) 
        #form = DtlsForm()  
                                    
    #return render_to_response('ptdetails_form.html',
    #                             {'form':form, 'add':True}) 
    return render_to_response('dx_custom_form.html',
                                 {'form':form, 'add':True}) 
    
        
def list_abstract(request):
    # list all pts pending prescreen
    error = False
    form = SearchForm()
    patients = []
    show_results = False
    patients = Ptmaster.objects.filter(absstatus__exact='PRESCREENOK')
                
    variables = RequestContext(request, {
    'form': form,
    'patients': patients,
    'show_results': True,
    'show_tags': True,
    'show_user': True,
    'error': error
    })
    if request.GET.has_key('ajax'):
        return render_to_response('prescreen_complete.html', variables)
    else:
        return render_to_response('prescreen_complete.html', variables)        
        
                                                                                                               
def search_patient(request):
    # AJAX search (via ssn) for existing patient(s) in Ptmaster table
    error = False
    form = SearchForm()
    patients = []
    show_results = False
    if 'query' in request.GET:
        show_results = True
        query = request.GET['query'].strip()
        if query:
            form = SearchForm({'query' : query})
            patients = Ptmaster.objects.filter(ssn__startswith=query)
        else:
            error = True
            
    variables = RequestContext(request, {
    'form': form,
    'patients': patients,
    'show_results': show_results,
    'show_tags': True,
    'show_user': True,
    'error': error
    })
    
    # ?? Select different template based on where user came from
    # (e.g. if user selected DX Assignment then need to link there next)
    if request.GET.has_key('ajax'):
        return render_to_response('ptmaster_list.html', variables)
    else:
        return render_to_response('search.html', variables)
        
def test(request):

    # handle test form
    form = TForm()      # Create Unbound form
    # How to set initial values??
    form.name = 'aaa'
    
    #assert False # for debugging

#    variables = RequestContext(request, {
#    'form': form,
#    'error': error
#    })
  
    return render_to_response('test_form.html', {'form': form,})
    
def search_patient_dx(request):
    # AJAX search (via PK) for matching records in the Ptdx table
    error = False
    caller = 'dx'
    # Get and confirmation message here and pass on
    patient = 0
    form = SearchForm()
    dxcodes = []
    show_results = False
    messages = ""
    
    # Check that user entered something in the Search field
    # Display error message otherwise
    
    if 'query' in request.GET:    
        #assert False
        show_results = True
        query = request.GET['query'].strip()
        if query:
            #form = SearchForm({'query' : query})
            form = SearchForm({'query' : query, 'messages' : messages})
            # lookup that spans relationships (implicit join)
            dxcodes = Ptdx.objects.filter(ptmaster__ssn__startswith=query) 
            try: 
                patient = dxcodes[0].ptmaster_id
            except ValueError:
                # no data found
                error = True
        else:
            # User failed to enter a search value
            #assert False
            error = True

    # get conf text from (from url parm  (PATH_INFO) or session object)            
	#msg = urlparse.urlparse(request.META.get('HTTP_REFERER', None)).path.split('/')[-1]
    #pathinfo = request.META.get('PATH_INFO', None).split('/')
    #try:    
    #    confirmation = pathinfo[2]
    #except ValueError:
    #    confirmation =""
        
    # retrieve session info  - then clear it
    confirmation = "" 
    msgtext = ""     
    try:
        confirmation += request.session['confirm']
        del request.session['confirm']
    except (KeyError, ValueError):
        pass
        
    # Add Confirmation Messages to context for display
    variables = RequestContext(request, {
    'form': form,
    'caller': caller,                
    'dxcodes': dxcodes,
    'patient': patient,
    'show_results': show_results,
    'show_tags': True,
    'show_user': True,
    'error': error,
    'msgs': confirmation
    })
        
    if request.GET.has_key('ajax'):
        # check for error
        #assert False
        #return render_to_response('dx_list.html', variables)
        if error:
            #pass
            return render_to_response('dx_list.html', variables) 
            #return HttpResponseRedirect('/dxsearch')                       
        else:
            return render_to_response('dx_list.html', variables)            
    else:
        #assert False
        # initial display of search form
        return render_to_response('search.html', variables)    
        
   
def search_patient_pr(request):
    # AJAX search (via PK) for matching records in the Ptdx table
    error = False
    caller = 'pr'
    form = SearchForm()
    patients = []
    show_results = False
    if 'query' in request.GET:
        show_results = True
        query = request.GET['query'].strip()
        if query:
            form = SearchForm({'query' : query})
            patients = Ptmaster.objects.filter(ssn__startswith=query)            
        else:
            error = True
            
    variables = RequestContext(request, {
    'form': form,
    'caller': caller,        
    'patients': patients,
    'show_results': show_results,
    'show_tags': True,
    'show_user': True,
    'error': error
    })
    
    # ?? Select different template based on where user came from
    # (e.g. if user selected DX Assignment then need to link there next)
    if request.GET.has_key('ajax'):
        return render_to_response('prescreen_list.html', variables)
    else:
        return render_to_response('search.html', variables)   
        
        
def search_patient_ab(request):
    l_type = 'ABLIST'
    return search_generic (request, l_type)


def search_generic(request, l_type):

    # Allow user to edit/add dx entry for selected patient
    # Need to receive a patient id
    # Display list of patients - link to dx list - allow edit/add
    # from this list
    
    # these templates are similar, except for the links that reference subsequent pages 
    if l_type == 'DXLIST':
        next = 'dx_list.html'
        
    if l_type == 'ABLIST':
        next = 'abstract_list.html'

    if l_type == 'PRLIST':
        next = 'prescreen_list.html'
                        
    # AJAX search (via ssn) for existing patient(s) in Ptmaster table
    error = False
    form = SearchForm()
    patients = []
    show_results = False
    if 'query' in request.GET:
        show_results = True
        query = request.GET['query'].strip()
        if query:
            form = SearchForm({'query' : query})
            patients = Ptmaster.objects.filter(ssn__startswith=query)
        else:
            error = True
            
    variables = RequestContext(request, {
    'form': form,
    'patients': patients,
    'show_results': show_results,
    'show_tags': True,
    'show_user': True,
    'error': error,
    'l_type': l_type,
    'messages': 'aaaa'
    })
    
    #assert False
    # How does this get set?
    if request.GET.has_key('ajax'):
        return render_to_response(next, variables)
    else:
        return render_to_response('search.html', variables)
        #return render_to_response(next, variables)
                

def  get_icd9_codes(request):
    # Ajax request to lookup diag codes - return space filled list
    # retrieve limited match results
    if 'q' in request.GET:

	# how to escape a string in ORM query ??
	# strip off the leading/trailing quote chars

	q1 = "\'" + request.GET['q']
	dxcodes = Icd9Base.objects.filter(icd9cm_code__istartswith=q1)[:100]
	
	#dxcodes = Icd9Base.objects.filter(icd9cm_code__istartswith=request.GET['q'])[:100]	
	#dxcodes = Icd9Base.objects.filter(icd9cm_code__istartswith=request.GET['q'])[:10]
	#dxcodes = Icd9Base.objects.filter(short_description__istartswith=request.GET['q'])[:100]
	#dxcodes = Icd9Base.objects.filter(icd9cm_code__contains=request.GET['q'])[:10]

	# ?? need to return Json data - one result per line  ??
	# strip off leading and trailing chars
	rslt = [dxcode.icd9cm_code[1:-1] + ';' + dxcode.short_description for dxcode in dxcodes]
	return HttpResponse(u'\n'.join(rslt))
	# these  below don't work
	#return  HttpResponse(u'\n\'.join([dxcode.icd9cm_code[1:-1] + ';' + dxcode.short_description for dxcode in dxcodes]))
	#return HttpResponse(u'\n'.join(dxcode for dxcode in dxcodes))
	#return  HttpResponse(u'\n\'.join([dxcode.icd9cm_code[1:-1] + ';' + dxcode.short_description for dxcode in dxcodes]))
	#return HttpResponse(u'\n'.join(dxcode.icd9cm_code[1:-1] for dxcode in dxcodes))
	# include descr in display also
	

	#return HttpResponse(u'\n'.join(dxcode.short_description for dxcode in dxcodes))
    return HttpResponse()    
        
        
def  get_icd9_codes_test (request):
    # Ajax request to lookup diag codes - return space filled list
    # retrieve limited match results
    if 'q' in request.GET:
	dxcodes = Dxtst.objects.filter(icd9code__startswith=request.GET['q'])[:15]
	# ?? need to return Json data - one result per line  ??
	return HttpResponse(u'\n'.join(dxcode.icd9code+ ';' + q.icd9dscr for dxcode in dxcodes))
    return HttpResponse()        


    
    
                                     
                                 
                                     


