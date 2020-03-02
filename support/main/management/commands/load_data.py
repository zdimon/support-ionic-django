from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from main.models import Page
from django.contrib.auth.models import User
from .utils import *

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Loading data into database....')
        try:
            p = Page.objects.get(name_slug='index')
        except:
            p = Page()
            p.name_slug = 'index'
            p.title = 'Welcome to the WEZOM support desktop!'
            p.content = 'You can send your message here.'
            p.save()
            print('Creating main page!')

        try:
            u = User.objects.get(username='admin')
        except:
            u = User()
            u.username = 'admin'
            u.is_active = True
            u.is_superuser = True
            u.is_staff = True
            u.save()
            u.set_password('admin')
            u.save()
            print('Creating superuser login admin password admin.')

        load_cat()
        #load_subcat()
        #load_test_task()
        #load_setting()