from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from account.models import Client, ClientChannel
import requests
from trello import TrelloClient
from support.settings import TRELLO_TOKEN, TRELLO_KEY

#loco = Client.objects.get(alias='locotrade')
client = TrelloClient(
    api_key=TRELLO_KEY,
    api_secret=TRELLO_TOKEN,
)

class Command(BaseCommand):

   
    def handle(self, *args, **options):
        
        boards = client.list_boards()
        for b in boards:
            for m in b.all_members():
                print('%s-%s' % (m.username, m.id))
            #break;
            