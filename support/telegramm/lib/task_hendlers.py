
from task.models import Category, SubCategory
from support.settings import TELEGRAMM_KEY, TELEGRAMM_NAME
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegramm.lib.utils import *
import telegram
from telegramm.dispacher import send_html_message
from telegramm.lib.messages import get_new_task_message, get_list_task_message, get_main_menu, get_change_status_message, get_want_file_message
from telegramm.lib.utils import get_last_telegramm_task_or_create
from trelloapp.tasks import task_export_comment_to_trello
from task.tornado_lib import ws_update_list, ws_update_task


bot = telegram.Bot(token=TELEGRAMM_KEY)

def build_menu(buttons,n_cols):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    return menu

def want_to_add_file_task(tsk,chat_id):
    msg = get_want_file_message()
    print(msg)
    #menu = get_main_menu()
    #send_html_message(chat_id,msg,reply_markup=menu)
    send_html_message(chat_id,msg) 

def finish_task(tsk,msg,chat_id):
    tsk.content = msg
    tsk.is_done_from_telegramm = True
    tsk.set_title()
    tsk.save()
    tsk.export()
    msg = get_new_task_message(tsk)
    menu = get_main_menu(tsk)
    send_html_message(chat_id,msg,reply_markup=menu)    
    ws_update_list()

def send_sub_category_menu(chat_id,cat):
    if has_subcategory(cat):
        msg = 'Выберите ПОД категорию заявки:'
        button_list = []
        for c in SubCategory.objects.all().order_by('id'):
            button_list.append(InlineKeyboardButton(c.title, callback_data='%s-%s' %(c.pk,'subcategory')))
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        bot.send_message(chat_id, msg, reply_markup=reply_markup)
    else:
        send_what_content(chat_id)

def send_category_menu(chat_id):
    msg = 'Выберите категорию заявки:'
    button_list = []
    for c in Category.objects.all().order_by('id'):
        button_list.append(InlineKeyboardButton(c.title, callback_data='%s-%s' % (c.pk,'category')))
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
    bot.send_message(chat_id, msg, reply_markup=reply_markup)    

    


def set_category(chat_id,cat_id):
    tsk = get_last_telegramm_task(chat_id)
    cat = Category.objects.get(pk=int(cat_id))
    tsk.category = cat
    tsk.save()
    send_html_message(chat_id,'Выбрана категория: <strong>%s</strong>' % cat.title)
    send_sub_category_menu(chat_id,cat)
    return tsk


def set_sub_category(chat_id,subcat_id):
    tsk = get_last_telegramm_task(chat_id)
    subcat = SubCategory.objects.get(pk=int(subcat_id))
    tsk.subcategory = subcat
    tsk.save()
    send_html_message(chat_id,'Выбрана подкатегория: <strong>%s</strong>' % subcat.title)
    send_what_content(chat_id)
    return tsk

def add_new_task(chat_id):
    tsk = get_last_telegramm_task_or_create(chat_id)
    #if not tsk.category:
    send_category_menu(chat_id)    

    
def add_comment(tsk,text,chat_id):
    tclient = ClientTelegramm.objects.get(chat_id=chat_id)
    c = Comment()
    c.task = tsk
    c.content = text
    c.author = tclient.name
    c.user = tclient.user
    c.is_support = tclient.user.profile.is_support
    c.save()
    task_export_comment_to_trello.delay(c)
    msg = 'Коментарий был добавлен к задаче %s' % tsk.title
    send_html_message(chat_id,msg)
    ws_update_task(tsk.id)

def send_change_status_message(task):
    cl = ClientTelegramm.objects.get(user=task.user)
    send_html_message(cl.chat_id,get_change_status_message(task))