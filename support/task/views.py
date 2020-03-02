from django.shortcuts import render, get_object_or_404
from .models import Task, Category, SubCategory, Comment
from .forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from support.settings import SITE_URL, MOBILE_URL
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files import File
from account.models import Client
from trelloapp.export_trello import export_file_to_trello
from trelloapp.tasks import task_export_file_to_trello
from main.models import Digest
from trelloapp.tasks import task_export_comment_to_trello
from telegramm.dispacher import send_message, send_image, send_document
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def nl2br(string, is_xhtml= True ):
    if is_xhtml:
        return string.replace('\n','<br />\n')
    else :
        return string.replace('\n','<br>\n')

def edit_task(request,pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные сохранены!')
        else:
            messages.error(request, 'Ошибка!')
            # do something.
    else:
        form = TaskForm(instance=task)

    return render(request,'task/edit_task.html', {'task': task, 'form': form})

def show_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    comments = Comment.objects.filter(task=task)
    comment = Comment(task=task, user=request.user)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            c = form.save()
            task_export_comment_to_trello.delay(c)
            messages.success(request, 'Данные сохранены!')
            return redirect('show_task', pk=task.id)
        else:
            messages.warning(request, 'Ошибка!')
    return render(request,'task/show_task.html', {'task': task, 'form': form, 'comments': comments})

######################################################################

def get_digest(request,site,lang):

    site = Client.get_client_by_host(site)
    if not site:
        return HttpResponse('Error, client does not exist!')
    digest = Digest.objects.all().order_by('-id')[0]
    context = {'digest': digest}
    tpl = 'task/digest_%s.html' % site.alias
    return render(request,tpl, context)


def get_task_list(request,site,lang,status):
    print(site)

    site = Client.get_client_by_host(site)
    user = Client.get_user(site)
    if not site:
        return HttpResponse('Error, client does not exist!')

    if status=='deleted':
        items = Task.objects.filter(source=user.profile.client.alias,is_deleted=True).order_by('-id')
    elif status=='all':
        items = Task.objects.filter(source=user.profile.client.alias,is_deleted=False).order_by('-id')
    else:
        items = Task.objects.filter(source=user.profile.client.alias,status=status,is_deleted=False).order_by('-id')
    
    context = {'items': items, 'site': SITE_URL}
    tpl = 'task/task_list_%s.html' % site.template
    return render(request,tpl, context)

def get_task_form(request,site,lang):

    site = Client.get_client_by_host(site)
    if not site:
        return HttpResponse('Error, client does not exist!')

    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    context = { 'categories': categories, 
                'subcategories': subcategories, 
                'site': SITE_URL,
                'client': site 
              }
    tpl = 'task/task_form_%s.html' % site.template
    return render(request,tpl, context)

def show_task_locotrade(request,site,lang,id):

    site = Client.get_client_by_host(site)
    if not site:
        return HttpResponse('Error, client does not exist!')

    task = Task.objects.get(pk=id)
    status_dict = []
    for s in Task.TYPE_CHOICES:
        status_dict.append({'value': s[0], 'name': s[1]})
    context = { 'task': task, 'site': SITE_URL, 
                'comments': task.comment_set.all(),
                'status_dict': status_dict}
    tpl = 'task/show_task_%s.html' % site.template
    return render(request,tpl, context)

def del_task(request,site,id):
    try:
        task = Task.objects.get(pk=id)
        task.is_deleted = True
        task.save()
    except:
        pass
    return HttpResponse('ok')

@csrf_exempt
def save_task(request):
    #import pdb; pdb.set_trace()
    
    if request.method == 'POST':
        site = request.POST.get('source')
        user = Client.get_user(site)
        client = Client.get_client_by_host(site)
        client.contact_email = request.POST.get('email')
        client.contact_phone = request.POST.get('phone')
        client.save()

        t = Task()
        t.title = request.POST.get('title')
        t.content = request.POST.get('content')
        t.contacts = '\n email: %s' % request.POST.get('email')
        t.content = nl2br(t.content)
        if len(request.POST.get('phone'))>2:
            t.contacts = t.contacts + '\n тел: %s' % request.POST.get('phone')
        t.category_id = request.POST.get('category')
        t.subcategory_id = request.POST.get('subcategory')
        t.source = user.profile.client.alias
        t.status = 'new'
        t.user = user
        t.save()
        t.export()
        #items = Task.objects.all()
        #tpl = 'task/task_list_%s.html' % site
        #context = {'items': items}
        #return render(request,tpl, context)
        return HttpResponse(t.id)
    else:
        return HttpResponse('OPTIONS')

@csrf_exempt
def save_comment(request):
    if request.method == 'POST':
        id_task = request.POST.get('task_id')
        content = request.POST.get('content')
        try:
            task = Task.objects.get(pk=id_task)
        except Exception as e:
            return {'status': 1, 'message': str(e)}
        user = task.user
        if len(content)>0:
            c = Comment()
            c.task = task
            c.author = request.POST.get('source')
            c.content = content
            c.user = user
            c.save()
            task_export_comment_to_trello.delay(c)
            if c.user:
                msg = 'Задача "%s" добавлен комментарий: \n *%s*' % (c.task.title, c.content)
                send_message(c.user,msg)
        return HttpResponse(task.pk)
    else:
        return HttpResponse('OPTIONS')

def get_task_comment(request,site,lang,id):

    site = Client.get_client_by_host(site)
    if not site:
        return HttpResponse('Error, client does not exist!')

    task = Task.objects.get(pk=id)
    context = {'comments': task.comment_set.all()}
    tpl = 'task/task_comments_%s.html' % site.alias
    return render(request,tpl, context)


@csrf_exempt
def save_file(request):
    if request.method == 'POST':
        print(request.FILES)
        id = request.POST.get('task_id')
        task = Task.objects.get(pk=id)
        uploaded_file = request.FILES['file']
        filename = uploaded_file.name
        file_ext = filename[-4:]
        c = Comment()
        c.task = task
        c.is_file = True
        c.save()
        f = File(uploaded_file)
        fname = '%s.%s' % (c.id,file_ext)
        c.file.save(fname, f)
        #export_file_to_trello(c)
        #import pdb; pdb.set_trace()
        task_export_file_to_trello.delay(c)
        if c.user:
            send_message(c.user,msg)
            if c.is_image():
                send_image(c.user,c.file.path)
            else:
                send_document(c.user,c.file.path)
        #import pdb; pdb.set_trace()
        return HttpResponse(task.id)
    else:
    #import pdb; pdb.set_trace()
        return HttpResponse('ok')

@csrf_exempt
def update_task(request):
    if request.method == 'POST':
        print(request.POST)
    return HttpResponse('ok')


def manage_task(request,id,user_id):
    user = User.objects.get(pk=user_id)
    user.backend='django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return redirect('show_task', pk=id)
