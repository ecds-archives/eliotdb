from django.db import models
from django.template.defaultfilters import escape
from django.core.urlresolvers import reverse

class Name(models.Model):
    objects = models.Manager()
    tei_id = models.CharField(max_length=50, unique=True, verbose_name="Tei Id")
    surname = models.CharField(max_length=100, blank=True, verbose_name="Last Name")
    forename = models.CharField(max_length=100, blank=True, verbose_name="First Name(s)")
    alt_names = models.CharField(max_length=100, null=True, blank=True, verbose_name="Alternate Name(s)") 
    birth = models.CharField(max_length=20, blank=True)
    death = models.CharField(max_length=20, blank=True)
    viaf = models.CharField(max_length=100, null=True, blank=True, verbose_name="VIAF", help_text="Virtual International Authortiy File")
    odnb = models.CharField(max_length=100, blank=True, verbose_name="ODNB", help_text="Oxford Dictionary of National Biography")
    seg = models.TextField(max_length=1000, blank=True, verbose_name="Tagged Segment") 
    footnote = models.TextField(max_length=5000, blank=True, verbose_name="Complete Footnote")
    notes = models.TextField(max_length=5000, blank=True, verbose_name="Encoder Notes")
    class Meta:
        db_table = 'names'
        ordering = ['tei_id']
    def __unicode__(self):
        return self.tei_id
    def has_viaf(self):
        if self.viaf != None and self.viaf != "":
            return True
        else:
            return False
    has_viaf.boolean = True
    has_viaf.short_description = "VIAF"
    def has_odnb(self):
        if self.odnb != None and self.odnb != "":
            return True
        else:
            return False
    has_odnb.boolean = True
    has_odnb.short_description = "ODNB"
    

class Document(models.Model):
    objects = models.Manager()
    tei_id = models.CharField(max_length=200, unique=True, verbose_name="Tei Id")
    eliot_vol = models.CharField(max_length=200, blank=True, verbose_name="Volume")
    eliot_part = models.CharField(max_length=200, blank=True, verbose_name="Part")
    eliot_period = models.CharField(max_length=200, blank=True, verbose_name="Period")
    eliot_toc = models.CharField(max_length=200, blank=True, verbose_name="Table of Contents #")
    src_title_a = models.CharField(max_length=200, blank=True, verbose_name="Article Title")
    src_title_m = models.CharField(max_length=200, blank=True, verbose_name="Monograph Title")
    src_title_j = models.CharField(max_length=200, blank=True, verbose_name="Journal Title")
    src_date = models.CharField(max_length=200, blank=True, verbose_name="Date")
    src_pub = models.CharField(max_length=200, blank=True, verbose_name="Publisher")
    src_plc = models.CharField(max_length=200, blank=True, verbose_name="Pub Place")
    src_vol = models.CharField(max_length=200, blank=True, verbose_name="Pub Volume")
    src_pg = models.CharField(max_length=200, blank=True, verbose_name="Pages")
    src_id = models.CharField(max_length=200, blank=True, verbose_name="Gallup #")
    alt1_title_a = models.CharField(max_length=200, blank=True, verbose_name="Article Title", help_text="Alt Source 1")
    alt1_title_m = models.CharField(max_length=200, blank=True, verbose_name="Monograph Title", help_text="Alt Source 1")
    alt1_title_j = models.CharField(max_length=200, blank=True, verbose_name="Journal Title", help_text="Alt Source 1")
    alt1_date = models.CharField(max_length=200, blank=True, verbose_name="Date", help_text="Alt Source 1")
    alt1_pub = models.CharField(max_length=200, blank=True, verbose_name="Publisher", help_text="Alt Source 1")
    alt1_plc = models.CharField(max_length=200, blank=True, verbose_name="Pub Place", help_text="Alt Source 1")
    alt1_vol = models.CharField(max_length=200, blank=True, verbose_name="Pub Volume", help_text="Alt Source 1")
    alt1_pg = models.CharField(max_length=200, blank=True, verbose_name="Pages", help_text="Alt Source 1")
    alt1_id = models.CharField(max_length=200, blank=True, verbose_name="Gallup #", help_text="Alt Source 1")
    alt2_title_a = models.CharField(max_length=200, blank=True, verbose_name="Article Title", help_text="Alt Source 2")
    alt2_title_m = models.CharField(max_length=200, blank=True, verbose_name="Monograph Title", help_text="Alt Source 2")
    alt2_title_j = models.CharField(max_length=200, blank=True, verbose_name="Journal Title", help_text="Alt Source 2")
    alt2_date = models.CharField(max_length=200, blank=True, verbose_name="Date", help_text="Alt Source 2")
    alt2_pub = models.CharField(max_length=200, blank=True, verbose_name="Publisher", help_text="Alt Source 2")
    alt2_plc = models.CharField(max_length=200, blank=True, verbose_name="Pub Place", help_text="Alt Source 2")
    alt2_vol = models.CharField(max_length=200, blank=True, verbose_name="Pub Volume", help_text="Alt Source 2")
    alt2_pg = models.CharField(max_length=200, blank=True, verbose_name="Pages", help_text="Alt Source 2")
    alt2_id = models.CharField(max_length=200, blank=True, verbose_name="Gallup #", help_text="Alt Source 2")
    alt3_title_a = models.CharField(max_length=200, blank=True, verbose_name="Article Title", help_text="Alt Source 3")
    alt3_title_m = models.CharField(max_length=200, blank=True, verbose_name="Monograph Title", help_text="Alt Source 3")
    alt3_title_j = models.CharField(max_length=200, blank=True, verbose_name="Journal Title", help_text="Alt Source 3")
    alt3_date = models.CharField(max_length=200, blank=True, verbose_name="Date", help_text="Alt Source 3")
    alt3_pub = models.CharField(max_length=200, blank=True, verbose_name="Publisher", help_text="Alt Source 3")
    alt3_plc = models.CharField(max_length=200, blank=True, verbose_name="Pub Place", help_text="Alt Source 3")
    alt3_vol = models.CharField(max_length=200, blank=True, verbose_name="Pub Volume", help_text="Alt Source 3")
    alt3_pg = models.CharField(max_length=200, blank=True, verbose_name="Pages", help_text="Alt Source 3")
    alt3_id = models.CharField(max_length=200, blank=True, verbose_name="Gallup #", help_text="Alt Source 3")
    notes = models.TextField(max_length=5000, blank=True)
    class Meta:
        db_table = 'documents'
        ordering = ['tei_id']
    def __unicode__(self):
        return self.tei_id
    def get_title(self):
        if self.src_title_a != None and self.src_title_a != '':
            return self.src_title_a
        else:
            return self.src_title_m

class Mention(models.Model):
    objects = models.Manager()
    name = models.ForeignKey(Name, to_field='tei_id', verbose_name="Name Id")
    document = models.ForeignKey(Document, to_field='tei_id', verbose_name="Document Id")
    type = models.CharField(max_length=20)
    class Meta:
        db_table = 'mentions'
        ordering = ['name', '-type', 'document']
    def __unicode__(self):
        return self.type
    
