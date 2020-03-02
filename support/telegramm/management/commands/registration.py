from telegramm.dispacher import send_html_message
from telegramm.models import ClientTelegramm
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegramm.lib.task_hendlers import build_menu
import telegram
from support.settings import TELEGRAMM_KEY, TELEGRAMM_NAME
from task.models import Category, SubCategory
bot = telegram.Bot(token=TELEGRAMM_KEY)
from django.contrib.auth.models import User
from account.models import PreAccount, Client2User, Client

def register_user(client):
    try:
        user = User.objects.get(username=client.email)
        client.user = user
        client.save()
    except:
        user = User()
        user.username = client.email
        user.set_password('123')
        user.is_active = True
        user.save()
        user.profile.is_support = True
        user.profile.save()
    return user


def process(client,input):


    if not client.name:
        client.name = input
        client.save()
        print('Save name %s' % input)
        msg = 'Спасибо %s! \n Теперь введите контактный email пожалуйста!' % client.name
        send_html_message(client.chat_id,msg)
        return True

    if not client.email:
        client.email = input
        client.save()
        print('Save email %s' % input)
        msg = 'Теперь введите Ваш номер телефона!'
        send_html_message(client.chat_id,msg)
        return True

    if not client.phone:
        client.phone = input
        client.save()
        print('Save phone %s' % input)
        msg = 'Отлично! \n Для завершения регистрации введите адрес сайта.'
        send_html_message(client.chat_id,msg)
        return True

    if not client.domain:
        input = input.replace('http://','')
        input = input.replace('https://','')
        input = input.replace('/','')
        client.domain = input
        client.is_done = True
        client.save()
        user = register_user(client)
        client.user = user
        client.save()
        bind_tclient_toclient(client)
        print('Save domain %s' % input)
        msg = 'Благодарим за регистрацию! Для добавления новой заявки нажмите кнопку'
        #send_html_message(client.chat_id,msg)
        button_list = []
        button_list.append(InlineKeyboardButton('Добавить заявку', callback_data='add_new_task'))
        #for c in Category.objects.all().order_by('id'):
        #    button_list.append(InlineKeyboardButton(c.title, callback_data='%s-%s' %(c.pk,'subcategory')))
        #print(button_list)
        menu = build_menu(button_list, n_cols=1)
        reply_markup = InlineKeyboardMarkup(menu)
        print(menu)
        
        #button_list=[[InlineKeyboardButton('Добавить заявку')]]
        #reply_markup = InlineKeyboardMarkup(button_list)
        bot.send_message(client.chat_id, msg, reply_markup=reply_markup)
        return True


    '''
    if not client.name:
        msg = 'Введите ваше имя. Как к вам обращаться?'
        send_html_message(client.chat_id,msg)
        return True
    if not client.email:
        msg = 'Введите ваш адресс электронной почты.'
        send_html_message(client.chat_id,msg)
        return True
    if not client.phone:
        msg = 'Введите ваш контактный номер телефона.'
        send_html_message(client.chat_id,msg)
        return True
    '''

def bind_tclient_toclient(tc):

    try:
        ac = PreAccount.objects.get(email=tc.email)
        client = ac.client
    except Exception as e:
        print(str(e))
        client = Client.objects.get(alias='SupportTelegramBot')

    c2u = Client2User()
    c2u.client = client
    c2u.user = tc.user
    c2u.save()
    pr = tc.user.profile
    pr.client = client
    pr.name = tc.name
    pr.email = tc.email
    pr.phone = tc.phone
    pr.save()

        



def create_client(login,chat_id):
    try:
        ClientTelegramm.objects.get(chat_id=chat_id)
    except:
        c = ClientTelegramm()
        c.login = login
        c.chat_id = chat_id
        c.save()
        msg = 'Создан новый аккаунт логин: <strong>(%s)</strong> id комнаты: <strong>%s</strong> \n Для продолжения регистрации скажите как к вам обращаться?' % (login,chat_id)
        send_html_message(chat_id,msg)
        return c

def check_registration(login,chat_id,input):
    try:
        c = ClientTelegramm.objects.get(login=login)
        if not c.is_done:    
            process(c,input)
    except Exception as e:
        print(str(e))
        c = create_client(login,chat_id)
    if c.is_done:
        return True
    else:
        return False
