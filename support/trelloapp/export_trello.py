import requests
from support.settings import TRELLO_KEY, TRELLO_SECRET, TRELLO_TOKEN, TRELLO_PRJ, SITE_URL
from trello.card import Card
#from trello import TrelloApi
#trello = TrelloApi(TRELLO_KEY)
from account.models import Client, ClientChannel
from trello import TrelloClient
from .utils import get_trello_client, get_board, get_new_list
from telegramm.models import ClientTelegramm


def add_hook(card,task):
    client = get_trello_client(task)
    from task.models import Log
    url = 'https://api.trello.com/1/tokens/%s/webhooks/?key=%s' % (client.api_secret,client.api_key) 
    data = {
        'callbackURL': '%s/trello/hook' % SITE_URL,
        'idModel': card.id,
        'description': 'adding hook'
    }
    rez = requests.post(url,data=data)
    l = Log()
    l.name = 'Adding trello hook'
    l.desc = rez.text
    l.save()
    print(rez.text) 


def export_file_to_trello(comment,task=None):
    from task.models import Task
    #import time
    #time.sleep(5)
    if task==None:
        task = Task.objects.get(pk=comment.task_id)
        #print('Exporting file %s!' % comment.get_file_uri())
    client = get_trello_client(task)
    #cid = comment.task.get_trello_id()
    print('Exporting file: Getting card id task:%s id comment: %s file: %s' % (task.trello_id, comment.task_id, comment.get_file_uri()))
    #try:
    print(task)
    c = client.get_card(task.trello_id)
    card = c.attach(url=comment.get_file_uri())
    #print(card)
    comment.trello_id = card['id']
    comment.save()
    #except Exception as e:
    #    print(str(e))


def export_comment_to_trello(comment):
    client = get_trello_client(comment.task)
    cid = comment.task.trello_id
    print('Exporting comment %s to trello trello id %s' % (comment.id, cid))
    comment.content = comment.content + '\n Автор: %s' % comment.user.profile.name
    try:
        c = client.get_card(cid)
        tcom = c.comment(comment.content)
        #print(tcom)
        comment.trello_id = tcom['id']
        comment.save()
    except Exception as e:
        print("ERROR: %s" % str(e))



def export_task_files(task):
    from task.models import Comment, Task
    for c in Comment.objects.filter(task=task,is_trello_exported=False,is_file=True):
        #export_comment_to_trello(c)
        print('Task trello id %s' % task.trello_id)
        export_file_to_trello(c,task)


def export_task_to_trello(task):
    try:
        client = Client.objects.get(location=task.source)
    except:
        if task.trello_board_name:
            client = Client.objects.get(alias=task.trello_board_name)
        else:
            client = Client.objects.get(alias='SupportTelegramBot')
    #import pdb; pdb.set_trace()
    print('Exporting task %s to trello' % task.id)
    board = get_board(task,client)
    lst = get_new_list(board.list_lists())
    content = str(task.content)
    content = content+'\n Источник: '+str(task.source)

    try:
        user = ClientTelegramm.objects.get(user=task.user)
        content = content+'\n Контакты: \n %s \n %s \n %s' % (user.name, user.phone, user.email)
    except Exception as e:
        print(str(e))
        content = content+'\n Контакты: \n %s \n %s \n %s' % (client.contact_name,client.contact_phone,client.contact_email)

    card = lst.add_card(task.title,content)
    task.is_trello_exported = True
    task.trello_link = card.url
    task.trello_id = card.id
    task.save()
    add_hook(card,task)
    #export_task_files(task)
    #export_task_comments(task)
    #board = trello.boards.get('4E1nBqW1')
    #import pdb; pdb.set_trace()
    #print (board.list_lists())
    #print(all_boards)





    

  