from django.contrib import admin
from eliotdb_app.models import Name, Document, Mention

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

admin.site.register(Mention, MentionAdmin)
