from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from main.models import Page
from django.contrib.auth.models import User
from account.models import Client

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Updating clients')
        for c in Client.objects.all():
            c.trello_key = 'd07648e64fb3eb301e7fbd34cef497c0'
            c.trello_token = '15ce75d2790a32d3b04fdcacf61a92673889ae924ae5f89a56d70cfacd025673'
            c.save()