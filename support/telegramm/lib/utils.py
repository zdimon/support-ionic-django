# https://github.com/python-telegram-bot/python-telegram-bot
from task.models import Task, Category, SubCategory, Comment
from account.models import Profile, Client
import telegram
from support.settings import TELEGRAMM_KEY, TELEGRAMM_NAME
from telegramm.dispacher import send_html_message
from telegramm.lib.messages import get_list_task_message, get_add_file_message
from django.core.files import File
from trelloapp.tasks import task_export_comment_to_trello, task_export_task_to_trello, task_export_file_to_trello
bot = telegram.Bot(token=TELEGRAMM_KEY)
from telegramm.models import ClientTelegramm
from account.models import Client2User

def has_subcategory(cat):
    cnt = SubCategory.objects.filter(category=cat).count()
    if cnt>0:
        return True
    else:
        return False


def send_what_content(chat_id):
    msg = 'Опишите суть проблемы'
    bot.send_message(chat_id, text=msg)

def send_categories(chat_id):
    msg = 'Введите номер категории заявки:'
    for c in Category.objects.all().order_by('id'):
        msg += '\n %s. %s' % (c.pk,c)
    bot.send_message(chat_id, text=msg)    


def send_subcategories(chat_id, tsk):
    msg = 'Введите номер ПОДкатегории заявки:'
    for c in SubCategory.objects.filter(category=tsk.category).order_by('id'):
        msg += '\n %s. %s' % (c.pk,c)
    bot.send_message(chat_id, text=msg)


def get_last_telegramm_task(chat_id):
    #import pdb; pdb.set_trace()
    try:
        user = ClientTelegramm.objects.get(chat_id=chat_id)
        t =  Task.objects.get(user=user.user, is_active=True)
        return t
    except:
        return False

def get_task_by_id(id):
    try:
        return Task.objects.get(pk=int(id))
    except:
        return False

def activate_task_by_id(id,chat_id):
    rez = get_task_by_id(id)
    if rez:
        rez.set_active()
        send_html_message(chat_id, get_list_task_message(chat_id))
    else:
        send_html_message(chat_id,'Заявка с номером %s не найдена!' % id)


def get_last_telegramm_task_or_create(chat_id):

    try:
        t =  Task.objects.get(telegramm_room=chat_id, is_done_from_telegramm=False)
    except:
        #prof = Profile.objects.get(telegram_room=chat_id)
        tclient = ClientTelegramm.objects.get(chat_id=chat_id)
        u2c = Client2User.objects.get(user=tclient.user)
        #import pdb; pdb.set_trace()
        t = Task()
        t.user=tclient.user
        t.source = tclient.user.profile.client.alias
        t.telegramm_room = str(chat_id)
        t.is_from_telegramm = True
        t.trello_board_name = tclient.trello_board_name
        t.set_active()
        t.save()



    return t


def add_file_to_active_task(chat_id, file):
    tsk = get_last_telegramm_task(chat_id)
    if not tsk:
        send_html_message(chat_id,'Ошибка! Активной задачи не найдено!')
        #import pdb; pdb.set_trace()
    else:
        c = Comment()
        c.user = tsk.user
        c.task = tsk
        c.content = ''
        c.save()
        extar = file.split('.')
        filename = '%s.%s' % (c.id,extar[len(extar)-1])
        #import pdb; pdb.set_trace()
        with open(file, 'rb') as doc_file:
            c.file.save(filename, File(doc_file), save=True)
        c.save()
        send_html_message(chat_id,get_add_file_message())
        task_export_file_to_trello(c)