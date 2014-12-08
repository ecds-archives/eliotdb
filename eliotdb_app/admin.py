from django.contrib import admin
from eliotdb_app.models import Name, Document, Mention
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import csv
from itertools import chain

class MentionsInline(admin.TabularInline):
    model = Mention
    extra = 1

class NameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['tei_id', 'surname', 'forename', 'alt_names', 'birth', 'death', 'viaf', 'odnb']}),
        ('Editor Notes', {'fields': ['seg', 'footnote'], 'classes': ['collapse']}),
        ('Encoder Notes', {'fields': ['notes'], 'classes': ['collapse']})
         ]
    list_display = ('tei_id', 'surname', 'forename', 'alt_names', 'birth', 'death', 'has_viaf', 'has_odnb')
    search_fields = ['tei_id', 'surname', 'alt_names']
    inlines = [MentionsInline]
admin.site.register(Name, NameAdmin)

class DocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['tei_id', 'eliot_vol', 'eliot_part', 'eliot_period', 'eliot_toc', 'src_title_a', 'src_title_m', 'src_title_j', 'src_date', 'src_pub', 'src_plc', 'src_vol', 'src_pg', 'src_id']}),
        ('Alternate Sources', {'fields': ['alt1_title_a', 'alt1_title_m', 'alt1_title_j', 'alt1_date', 'alt1_pub', 'alt1_plc', 'alt1_vol', 'alt1_pg', 'alt1_id', 'alt2_title_a', 'alt2_title_m', 'alt2_title_j', 'alt2_date', 'alt2_pub', 'alt2_plc', 'alt2_vol', 'alt2_pg', 'alt2_id', 'alt3_title_a', 'alt3_title_m', 'alt3_title_j', 'alt3_date', 'alt3_pub', 'alt3_plc', 'alt3_vol', 'alt3_pg', 'alt3_id'], 'classes': ['collapse']}),
        ]
    def get_title(self, obj):
        if obj.src_title_a != None and obj.src_title_a != '':
            return obj.src_title_a
        else:
            return obj.src_title_m
    get_title.short_description = "Title"
    list_display = ('tei_id', 'get_title', 'src_date')
    search_fields = ['tei_id', 'src_title_a', 'src_title_m']
    inlines = [MentionsInline]

admin.site.register(Document, DocumentAdmin)

class MentionAdmin(admin.ModelAdmin):
    def get_name(self, obj):
        if obj.name.forename:
            return obj.name.surname + ', ' + obj.name.forename
        else:
            return obj.name.surname
    get_name.short_description = "Name"
   
    readonly_fields = ('name', 'get_name', 'document')
    list_display = ('type', 'name', 'get_name', 'document')
    search_fields = ['name__tei_id', 'document__tei_id']

    #admin.site.register(Mention, MentionAdmin)

def volume_index(vol_name):
    context = {}
    doc_list = []
    docs = Document.objects.order_by().values_list('tei_id', flat=True).filter(eliot_vol__contains=(vol_name + ':'))
        
    all_mentions = Mention.objects.order_by('name', '-type').filter(document__in=docs).select_related()
    first_mentions = all_mentions.filter(type='first')
    all_names = sorted(list(set(all_mentions.values_list('name', flat=True).distinct())))
    index = []
    for name in all_names:
        fm = first_mentions.filter(name=name)
        adds = all_mentions.filter(name=name).filter(type='additional')
        item = list(chain(fm, adds))
        index.append(item) 

    context['vol_name'] = vol_name
    context['first_mentions'] = first_mentions
    context['all_mentions'] = all_mentions
    context['all_names'] = all_names
    context['index'] = index
    context['docs'] = docs
    
    return context

# def volume_csv(request, context):
#     download_name = context['vol_name'] + '.csv'
#     response = HttpResponse(mimetype='text/csv')
#     response['Content-Disposition'] = 'attachment;filename=download_name'

#     writer = csv.writer(response)
#     writer.writerow(['Name', 'Documents'])
#     for name in context['index']:
#         first_mention = name[0]
#         name = first_mention.name.long_form
#         add_mentions = []
#         try:
#             for mention in name[1:]:
#                 doc = mention.document.stripped_id
#                 add_mentions.append(mention)
#                 add_mentions = ', '.join(add_mentions)
#         except:
#             add_mentions = ''
#         docs = '%s, %s' % (first_mention.document.stripped_id, add_mentions)
#         writer.writerow([name, docs])
#     return response

def volume_one_names(request):
    context = volume_index('Volume I')
    return render_to_response('admin/volume_names.html', context, context_instance=RequestContext(request))
admin.site.register_view('volume_one_names', 'Volume I Index', view=volume_one_names)

def volume_two_names(request):
    context = volume_index('Volume II')       
    return render_to_response('admin/volume_names.html', context, context_instance=RequestContext(request))
admin.site.register_view('volume_two_names', 'Volume II Index', view=volume_two_names)

def volume_three_names(request):
    context = volume_index('Volume III')       
    return render_to_response('admin/volume_names.html', context, context_instance=RequestContext(request))
admin.site.register_view('volume_three_names', 'Volume III Index', view=volume_three_names)

def volume_four_names(request):
    context = volume_index('Volume IV')       
    return render_to_response('admin/volume_names.html', context, context_instance=RequestContext(request))
admin.site.register_view('volume_four_names', 'Volume IV Index', view=volume_four_names)
