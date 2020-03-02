from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from support.settings import TRELLO_KEY, TRELLO_SECRET, TRELLO_TOKEN, TRELLO_PRJ
import requests
from trello import TrelloClient

client = TrelloClient(
    api_key='d07648e64fb3eb301e7fbd34cef497c0',
    api_secret='15ce75d2790a32d3b04fdcacf61a92673889ae924ae5f89a56d70cfacd025673',
)
from trelloapp.utils import get_board, get_new_list, get_trello_client
from trelloapp.export_trello import add_hook


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Test trello')
        board = client.list_boards()
        print(board)