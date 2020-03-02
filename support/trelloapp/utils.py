from account.models import Client, ClientChannel
from trello import TrelloClient
from support.settings import TRELLO_TOKEN, TRELLO_KEY

def get_trello_client(task):
    print('task %s' % task.source)
    wclient = Client.objects.get(alias=task.source)
    client = TrelloClient(
        api_key=wclient.trello_key,
        api_secret=wclient.trello_token,
    )
    return client

def get_project_id_by_location(location):
    try:
        cl = Client.objects.get(location=location)
        return cl.trello_project_id
    except Exception as e:
        print(str(e))
        return False


def get_board(task,client):
    tclient = get_trello_client(task)
    board = tclient.get_board(client.trello_project_id)
    return board




def get_new_list(lst):
    for l in lst:
        if l.name == 'Входящие' or 'В процессе рассмотрения':
            return l

def get_list_by_id(id):
    return ClientChannel.objects.get(key=id)