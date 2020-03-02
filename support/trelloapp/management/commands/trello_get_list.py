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

    #def add_arguments(self, parser):
    #    parser.add_argument('alias', type=str)

    def handle(self, *args, **options):
        #alias = options['alias']
        #print('Getting list of trello projects %s' % alias)
        #try:
        #    rec = Client.objects.get(alias=alias)
        #except:
        #    print('Error! %s does not exist' % alias)
        #    return False

      

        #board = client.get_board(loco.trello_project_id)
        boards = client.list_boards()
        for b in boards:
            print(b.id)
            print(b.name)
            try:
                br = Client.objects.get(alias=b.name)
            except Exception as e:
                br = Client()
                br.alias = b.name
                br.location = b.name
                br.trello_project_id = b.id
                br.save()
                print('creating %s' % b.name)
                print(str(e))

            lst =  b.list_lists()
            for l in lst:
                try:
                    ClientChannel.objects.get(client=br,name=l.name)
                except:
                    print('Creating list %s' % l.name)
                    ch = ClientChannel()
                    ch.name = l.name
                    ch.client = br
                    ch.key = l.id
                    ch.save()
                print(l.name)

        #lst = board.list_lists()
        #print(board)
        #print(lst)
        '''
        for l in lst:
            try:
                ch = ClientChannel.get(name=l.name)
            except:
                ch = ClientChannel()
                ch.client = rec
                ch.name = l.name
                ch.key = l.id
                if l.name == 'Входящие' or 'В процессе рассмотрения':
                    ch.is_new = True
                ch.save()
                print("Saving %s - %s" % (l.id,l.name))
        '''
        

        