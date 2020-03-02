from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as l
from django.contrib.auth import logout
from .forms import CustomerRegForm as RegForm, TelegrammRegForm
from django.contrib import messages
from jsonview.decorators import json_view
from .models import Profile
from django.contrib import messages
from support.settings import TELEGRAMM_KEY, WORKSECTION_KEY, TELEGRAMM_NAME
import hashlib
import requests
import sys

def import_worksection(request):
    project = '166584'
    page = '/project/%s/' % project
    action = 'get_projects'
    hashstr = '%s%s%s' % (page,action,WORKSECTION_KEY)
    print(hashstr)
    hash =  hashlib.md5(hashstr.encode()).hexdigest()
    url = 'https://wezom.worksection.com/api/admin/?action=get_projects&hash=%s' % hash
    data = requests.get(url)
    responce = data.text
    
    messages.success(request, 'Данные импортированы!')
    messages.success(request, '%s   %s' % (url, responce))
    return redirect('worksection') 


def worksection(request):
    return render(request,'account/worksection.html')

def test_telegramm(request):
    import telegram
    profile = request.user.profile
    bot = telegram.Bot(token=TELEGRAMM_KEY)
    bot.send_message(profile.telegram_room, text="Тестовое сообщение.")
    messages.success(request, 'Сообщение отправлено!')
    return redirect('profile') 

def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        
        #import pdb; pdb.set_trace()  
        if(not profile.telegram_login and len(request.POST.get('telegramm_login'))> 0):
            msg = '''
                Отлично! Теперь нажмите на <a target=_blank href="http://%s">Эту ссылку</a> и в программе телеграмм нажмите кнопку 'Start'
            ''' % TELEGRAMM_NAME
            messages.success(request, msg)
        profile.telegram_login = request.POST.get('telegramm_login')
        profile.w_login = request.POST.get('w_login')
        #profile.w_uid = request.POST.get('w_uid')
        #profile.w_password = request.POST.get('w_password')
        profile.save()
        messages.success(request, 'Данные сохранены!')
        
        return redirect('profile') 
    return render(request,'account/profile.html',{'profile': profile, 'bot_link': TELEGRAMM_NAME})

@json_view
def alogin(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        l(request, user)
        return { 'status': 0, 'message': 'Welcome!!!!' }
    else:
        return { 'status': 1, 'message': 'Login or password incorrect!!!' }


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

def registration(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TelegrammRegForm(request.POST)
        # check whether it's valid:
        if form.is_valid():  
            form.save()
            #messages.success(request, 'Bingo !!!')
            return redirect('registration_done')
        # if a GET (or any other method) we'll create a blank form
    form = TelegrammRegForm()

    return render(request,'account/registration.html',{'form': form})


def registration_done(request):

    return render(request,'account/registration_done.html', {'TELEGRAMM_NAME': TELEGRAMM_NAME})



