from django.db import models

class Name(models.Model):
    objects = models.Manager()
    tei_id = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    forename = models.CharField(max_length=100) 
    birth = models.CharField(max_length=20)
    death = models.CharField(max_length=20)
    viaf = models.CharField(max_length=100)
    odnb = models.CharField(max_length=100)
    seg = models.TextField(max_length=1000) 
    notes = models.TextField(max_length=5000)
    class Meta:
        db_table = 'names'

class Document(models.Model):
    tei_id = models.CharField(max_length=50)
    eliot_vol = models.CharField(max_length=100)
    eliot_part = models.IntegerField(max_length=1)
    eliot_period = models.IntegerField(max_length=4)
    eliot_toc = models.CharField(max_length=10)
    source_article = models.CharField(max_length=200)
    source_journal = models.CharField(max_length=200)
    source_date = models.CharField(max_length=30)
    source_vol = models.CharField(max_length=10)
    source_pages = models.CharField(max_length=10)
    gallup = models.CharField(max_length=10)
    notes = models.TextField(max_length=5000)
    class Meta:
        db_table = 'documents'

class Mention(models.Model):
    name = models.ForeignKey(Name)
    document = models.ForeignKey(Document)
    type = models.CharField(max_length=10)
    class Meta:
        db_table = 'mentions'
