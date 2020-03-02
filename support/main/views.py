from django.shortcuts import render, redirect
from .models import Page
from task.models import Task
from django.contrib.auth import authenticate, login as l
from django.contrib import messages
from django.urls import reverse
from account.models import create_client_if_not_exist
from support.settings import MOBILE_URL
from account.models import Client
from django.http import HttpResponse
# Create your views here.

welcome_message = '''Для подключения бота необходимо указать логин в телеграмме и нажать кнопку "Сохранить!" '''

def get_script(request,site,lang):
    if(request.META['REMOTE_HOST']):
        print(request.META['REMOTE_HOST'])
    #    create_client_if_not_exist(request.META['REMOTE_HOST'])
    #print(request.META['REMOTE_HOST'])
    try:
        cl = Client.objects.get(alias=site)
        context = {'site': site, 'lang': lang, 'mobile_url': MOBILE_URL, 'client_sign': cl.sign}
        return render(request,'script.js',context)
    except Exception as e:
        mes = str(e) 
        print(mes)
        return HttpResponse('alert("%s")' % mes)


def index(request):
    page = Page.objects.get(name_slug='index')
    tasks = []
    if request.user.is_authenticated:
        #tasks = Task.objects.filter(user=request.user).order_by('-is_active','-id')
        tasks = Task.objects.all().order_by('-is_active','-id')
        #if not request.user.profile.telegram_login:
        #    messages.warning(request, welcome_message)
        #    return redirect('profile')
    else:
        messages.warning(request, 'Нужно авторизоваться!')
        messages.success(request, 'Для входа используйте <a href="%s">гугл аккаунт</a>' % reverse('social:begin', args=['google-oauth2']) )
    return render(request,'main/index.html',{'page': page, 'tasks': tasks})



def login(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        l(request, user)
        return redirect('home')
    else:
        messages.warning(request, 'Error!!!!')
        return redirect('home')

def logoutme(request):
    logout(request)
    return redirect('home')
