from django.contrib import admin
from eliotdb_app.models import Name, Document, Mention

admin.site.register(Mention)

class NameAdmin(admin.ModelAdmin):
    list_display = ('tei_id', 'surname', 'forename', 'alt_names', 'birth', 'death', 'has_viaf', 'has_odnb')
    search_fields = ['tei_id', 'surname', 'alt_names']
    
admin.site.register(Name, NameAdmin)

class DocumentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['tei_id', 'eliot_vol', 'eliot_part', 'eliot_period', 'eliot_toc', 'src_title_a', 'src_title_m', 'src_title_j', 'src_date', 'src_pub', 'src_plc', 'src_vol', 'src_pg', 'src_id']}),
        ('Alternate Sources', {'fields': ['alt1_title_a', 'alt1_title_m', 'alt1_title_j', 'alt1_date', 'alt1_pub', 'alt1_plc', 'alt1_vol', 'alt1_pg', 'alt1_id', 'alt2_title_a', 'alt2_title_m', 'alt2_title_j', 'alt2_date', 'alt2_pub', 'alt2_plc', 'alt2_vol', 'alt2_pg', 'alt2_id', 'alt3_title_a', 'alt3_title_m', 'alt3_title_j', 'alt3_date', 'alt3_pub', 'alt3_plc', 'alt3_vol', 'alt3_pg', 'alt3_id'], 'classes': ['collapse']}),
    ]

admin.site.register(Document, DocumentAdmin)
