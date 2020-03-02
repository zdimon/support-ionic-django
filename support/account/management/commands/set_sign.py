from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from main.models import Page
from django.contrib.auth.models import User
from account.models import Profile, Client

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Setting sign')
        for p in Profile.objects.all():
            if not p.sign:
                p.set_sign()
        for p in Client.objects.all():
            if not p.sign:
                p.set_sign()