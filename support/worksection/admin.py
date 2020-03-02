from django.contrib import admin
from .models import WUser, WProject

class WProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'page', 'status']
    search_fields = ['name', 'page']

admin.site.register(WProject, WProjectAdmin)


class WUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']

admin.site.register(WUser, WUserAdmin)
