from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from main.models import Page
from django.contrib.auth.models import User
from account.models import Client

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Deleting clients')
        Client.objects.all().delete()