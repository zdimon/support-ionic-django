from django.shortcuts import render
from jsonview.decorators import json_view
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json 
from account.models import Profile, Client
from .utils import get_user_by_token
from task.models import Task
from .lib.serializer import serialize_task_list, serialize_task
from task.models import Task, Comment
from django.contrib.auth.models import User
from .models import get_task_list
import base64
from django.core.files.base import ContentFile
from trelloapp.tasks import task_export_file_to_trello, task_export_comment_to_trello

@json_view
def settings(request):
    return {'per_page': '10'}


@json_view
def task_list(request,filter='all'):
    out = {"status": 0, "tasks": []}
    #print(request.META)
    if request.method == "GET":
        token = request.META.get('HTTP_AUTHORIZATION').replace('Token ','')
        user = get_user_by_token(token)
        tasks = get_task_list(user,filter)
        out['tasks'] = serialize_task_list(tasks)
        out['filter'] = 'all'
        return out
    else:
        return out


@json_view
def show_task(request,task_id):
    out = {"status": 0, "task": {}}
    if request.method == "GET":
        task = Task.objects.get(pk=task_id)
        out['task'] = serialize_task(task)
        return out
    else:
        return out    



@csrf_exempt
@json_view
def enter_client(request):
    if request.method == "POST":
        
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)
        try:
            cl = Client.objects.get(sign=payload['sign'])
            return {"status": 0, "user_id": cl.user.pk, "user_sign": cl.user.profile.sign}
        except:
            return {"status": 1, "message": "Client not found!"}
        print(payload)
        return {"status": 0}
    else:
        return {"status": 0}


@csrf_exempt
@json_view
def enter_task(request):
    if request.method == "POST":
        
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)
        try:
            pr = Profile.objects.get(sign=payload['sign'])
            return {"status": 0, "user_id": pr.pk, "user_sign": pr.sign}
        except:
            return {"status": 1, "message": "Client not found!"}
        print(payload)
        return {"status": 0}
    else:
        return HttpResponse('Options')


# http://support.org/mobile_api/login_by_link/fedda421636cd36d7bddba5eace058a4/client

@csrf_exempt
def enter_client_by_link(request,sign):
    try:
        cl = Client.objects.get(sign=sign)
        cntx = {"status": 0, "user_id": cl.user.pk, "user_sign": cl.user.profile.sign}
    except:
        cntx = {"status": 1, "message": "Client not found!"}
    return render(request,'mobile_api/enter.html',cntx)

@csrf_exempt
@json_view
def save_comment(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION').replace('Token ','')
        user = get_user_by_token(token)
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)
        task = Task.objects.get(pk=payload['task_id'])
        c = Comment()
        c.task = task
        c.author = 'mobile app %s' % user.username
        c.content = payload['content']
        c.user = user
        c.save()  
        task_export_comment_to_trello(c)      
        
    else:
        return HttpResponse('Options')


@csrf_exempt
@json_view
def set_status(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)
        token = request.META.get('HTTP_AUTHORIZATION').replace('Token ','')
        user = get_user_by_token(token)
        task = Task.objects.get(pk=payload['task_id'])
        print('Set status %s' % payload['status'] )
        task.status = payload['status'] 
        task.save()        
        return {'status': 0, 'message': 'status changed OK'}
    else:
        return HttpResponse('Options')

@csrf_exempt
@json_view
def photo(request):
    out = {"status": 0, "task": {}}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)
        format, imgstr = payload['imgBase64'].split(';base64,')
        #print("format", format)
        print(payload)
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr))  
        file_name = payload['task_id']+"." + ext
        #print(payload)
        task = Task.objects.get(pk=payload['task_id'])
        token = request.META.get('HTTP_AUTHORIZATION').replace('Token ','')
        user = get_user_by_token(token)
        c = Comment()
        c.task = task
        c.author = 'mobile app %s' % user.username
        c.user = user
        c.save() 
        c.file.save(file_name, data, save=True)
        task_export_file_to_trello.delay(c)
        #task = Task.objects.get(pk=task_id)
        #out['task'] = serialize_task(task)
        return out
    else:
        return out   



@csrf_exempt
@json_view
def save_task(request):
    out = {"status": 0}
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        payload = json.loads(body_unicode)
        print(payload)
        token = request.META.get('HTTP_AUTHORIZATION').replace('Token ','')
        user = get_user_by_token(token)
        t = Task()
        t.title = payload['content']
        t.content = payload['content']
        #t.category_id = request.POST.get('category')
        #t.subcategory_id = request.POST.get('subcategory')
        #t.source = request.POST.get('source')
        t.source = user.profile.client.alias
        t.user = user
        t.save()
        out['task_id'] = t.id
        return out
    else:
        return out   