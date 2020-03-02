from django.contrib import admin
from .models import Profile, Client, ClientChannel, PreAccount, Client2User
from django.contrib.auth.models import User

class UserProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['alias', 'location', 'template', 'user', 'sign', 'trello_key', 'trello_token']

admin.site.register(Client, ClientAdmin)


class ClientChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'key', 'is_new', 'client']
    

admin.site.register(ClientChannel, ClientChannelAdmin)


class PreAccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'telegram', 'client', 'is_registered']
    

admin.site.register(PreAccount, PreAccountAdmin)


class Client2UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'client']
    

admin.site.register(Client2User, Client2UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'client', 'is_support']
    

admin.site.register(Profile, ProfileAdmin)
