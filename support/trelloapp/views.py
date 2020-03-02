from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json
from task.models import Task, Log, Comment
from .utils import get_list_by_id
from task.tornado_lib import ws_update_task
from telegramm.lib.task_hendlers import send_change_status_message

@csrf_exempt
def get_hook(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        #print(data)

        if 'commentCard' in data['action']['type']:
            print('Comment!!!!')
            card_id = data['action']['data']['card']['id']
            comment_id = data['action']['id']
            content = data['action']['data']['text']
            try:
                Comment.objects.get(trello_id=comment_id)
            except Exception as e:
                print('Card %s' % card_id)
                print(str(e))
                tsk = Task.objects.get(trello_id=card_id)
                c = Comment()
                c.content = content
                c.author = data['action']['memberCreator']['fullName']
                c.avatar = data['action']['memberCreator']['avatarUrl']
                c.task = tsk
                c.trello_id = card_id
                c.save()
                l = Log()
                l.name = 'Add comment from hook'
                l.desc = data
                l.save()
                ws_update_task(tsk.id)

        if 'addAttachmentToCard' in data['action']['type']:
            comment_id = data['action']['data']['attachment']['id']
            card_id = data['action']['data']['card']['id']
            try:
                Comment.objects.get(trello_id=comment_id)
            except Exception as e:
                tsk = Task.objects.get(trello_id=card_id)
                c = Comment()
                c.file_url_orig =  data['action']['data']['attachment']['previewUrl']
                c.file_url = data['action']['data']['attachment']['url']
                c.author = data['action']['memberCreator']['fullName']
                c.avatar = data['action']['memberCreator']['avatarUrl']
                c.task = tsk
                c.trello_id = comment_id
                c.save()   
                l = Log() 
                l.name = 'Add attachment from hook'
                l.desc = data
                l.save()
                ws_update_task(tsk.id)            
        
        if 'updateCard' in data['action']['type']:
            card_id = data['action']['data']['card']['id']
            print(card_id)
            try:
                tsk = Task.objects.get(trello_id=card_id)
                print(tsk)
            except:
                l = Log()
                l.name = 'Error to change status'
                l.desc = data
                l.save()

            try:
                lst_after = get_list_by_id(data['action']['data']['listAfter']['id'])
            except Exception as e:
                l = Log()
                l.name = 'Error to get list from trello'
                l.desc = str(e)
                l.save()
                
            try:
                tsk.status = data['action']['data']['listAfter']['name']
                tsk.save()
                ws_update_task(tsk.id)
                send_change_status_message(tsk)
            except:
                pass

            

    return HttpResponse('ok')