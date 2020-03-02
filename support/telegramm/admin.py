from django.contrib import admin
from .models import ClientTelegramm
# Register your models here.

class ClientTelegrammAdmin(admin.ModelAdmin):
    list_display = ['name', 'domain', 'login', 'chat_id', 'is_done']

admin.site.register(ClientTelegramm, ClientTelegrammAdmin)
