from django.contrib import admin
from .models import Setting, Publication, Document, Category, Work
# Register your models here.

admin.site.register(Setting)
admin.site.register(Publication)
admin.site.register(Document)
admin.site.register(Category)
admin.site.register(Work)
