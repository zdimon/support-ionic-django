from django.contrib import admin
from .models import *



class PageAdmin(admin.ModelAdmin):
    list_display = ['title','name_slug']

admin.site.register(Page, PageAdmin)


class DigestAdmin(admin.ModelAdmin):
    list_display = ['title','is_published']

admin.site.register(Digest, DigestAdmin)
