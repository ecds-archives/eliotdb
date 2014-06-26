import os
import re
from urllib import urlencode
import logging

from django.conf import settings
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.shortcuts import redirect
from django.db.models import Q

from eliotdb_app.models import Name, Document, Mention
from eliotdb_app.forms import SearchForm

logger = logging.getLogger(__name__)

def index(request):
  return render_to_response('index.html', context_instance=RequestContext(request))

def searchform(request):
    "Search by name."
    form = SearchForm(request.GET)
    response_code = None
    context = {'searchform': form}
    number_of_results = 100

    if form.is_valid():
        name = form.cleaned_data['name']
        names = Name.objects.only("tei_id", "surname", "forename", "birth", "death").filter(Q(surname__icontains="%s" % name) | Q(forename__icontains="%s" % name))

        context['name'] = name
        context['names'] = names
        context['name_count'] = len(names)

        response = render_to_response('search_results.html', context, context_instance=RequestContext(request))                         
    else:
        response = render(request, 'index.html', {"searchform": form})       
    if response_code is not None:
        response.status_code = response_code
    return response

def name_record(request, tei_id):
    name = Name.objects.get(tei_id__exact=tei_id)
    return render_to_response('name_record.html', {'name': name}, context_instance=RequestContext(request))
    
def edit_name(request, tei_id):
    name = Name.objects.get(tei_id__exact=tei_id)
    return render_to_response('edit_name.html', {'name' : name}, context_instance=RequestContext(request))

def save_name(request, tei_id):
    name = Name.objects.get(tei_id__exact=tei_id)
    return render_to_response('save_name.html', {'name' : name}, context_instance=RequestContext(request))

