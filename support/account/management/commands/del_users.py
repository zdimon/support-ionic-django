from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from main.models import Page
from django.contrib.auth.models import User
from account.models import Client, Profile

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Deleting User')
        for u in User.objects.all():
            try:
                u.delete()
            except:
                pass

        try:
            u = User.objects.get(username='admin')
        except:
            u = User()
            u.id = 1
            u.username = 'admin'
            u.is_active = True
            u.is_superuser = True
            u.is_staff = True
            u.save()
            u.set_password('admin')
            u.save()
            pr = u.profile
            pr.name = 'Админ Админович'
            pr.phone = '081234567'
            pr.save()

            print('Creating superuser login admin password admin.')