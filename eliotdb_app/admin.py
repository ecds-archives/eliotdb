from django.contrib import admin
from eliotdb_app.models import Name, Document, Mention

admin.site.register(Name)
admin.site.register(Document)
admin.site.register(Mention)
