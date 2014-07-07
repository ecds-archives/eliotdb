#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap, FlatPageSitemap, GenericSitemap

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from eliotdb_app.views import index, names, documents, searchform, name_record, edit_name, save_name

urlpatterns = patterns('eliotdb_app.views',
    url(r'^$', 'index', name='site-index'),
    url(r'^names$', 'names', name='names'),
    url(r'^documents$', 'documents', name='documents'),
    url(r'^search$', 'searchform', name='search'),
    url(r'^names/(?P<tei_id>[^/]+)$', 'name_record', name='name_record'),
    url(r'^names/(?P<tei_id>[^/]+)/edit$', 'edit_name', name='edit_name'),
    url(r'^(?P<tei_id>[^/]+)/save$', 'save_name', name='save_name'),
    )

if settings.DEBUG:
  urlpatterns += patterns(
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT } ),
)


