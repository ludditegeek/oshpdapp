# Create your views here.
import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

def hello(request):
    return HttpResponse("Hello Out There!!!")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def test(request):
    return render_to_response('test.html')

def homepage(request):
    return render_to_response('homepage.html')

def devtoolbag(request):
    return render_to_response('devtoolbag.html')

def cruddemo(request):
    return render_to_response('cruddemo.html')

def lgabout(request):
    return render_to_response('lgabout.html')

def gaebrowser(request):
    return render_to_response('gaebrowser.html')

def menutree(request):
    return render_to_response('menutree.html')

def datagrid(request):
    return render_to_response('datagrid.html')

def howtosyntax(request):
    return render_to_response('howtosyntax.html')

def howtofooter(request):
    return render_to_response('howtofooter.html')
