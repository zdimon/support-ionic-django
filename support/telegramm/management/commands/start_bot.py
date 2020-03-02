from django.core.management.base import BaseCommand, CommandError
import os
#from main.models import Setting
from account.models import Profile
from task.models import Category, SubCategory
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
import logging
from support.settings import TELEGRAMM_KEY, TELEGRAMM_NAME, SITE_URL, BASE_DIR
from telegramm.lib.utils import *
from telegramm.lib.help import send_help_message
from telegramm.dispacher import send_html_message
from telegramm.lib.messages import get_new_task_message, get_list_task_message
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegramm.lib.task_hendlers import set_category, set_sub_category, send_category_menu, finish_task, add_new_task, add_comment, want_to_add_file_task
from trelloapp.tasks import task_export_comment_to_trello, task_export_task_to_trello, task_export_file_to_trello
from telegramm.models import ClientTelegramm
from .registration import process, check_registration
from telegramm.lib.messages import get_main_menu

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    
bot = telegram.Bot(token=TELEGRAMM_KEY)




def fileHandler(update: Updater, context: CallbackContext):
    #response = 'Получил файл: ' + str(update.message.photo)
    #bot.send_message(chat_id=update.message.chat_id, text=response)
    #import pdb; pdb.set_trace()
    if(len(update.message.photo)>0):
        newFile = bot.get_file(update.message.photo[len(update.message.photo)-1])
        file_path = update.message.photo[len(update.message.photo)-1].get_file().file_path
        extw = file_path.split('/')
        fname = extw[len(extw)-1]
        #import pdb; pdb.set_trace()
        path = '%s/media/files/%s' % (BASE_DIR,fname)
        newFile.download(path)
        add_file_to_active_task(update.message.chat_id,path)
    if(update.message.document):
        newFile = bot.get_file(update.message.document)
        file_path = update.message.document.get_file().file_path
        extw = file_path.split('/')
        fname = extw[len(extw)-1]
        #import pdb; pdb.set_trace()
        path = '%s/media/files/%s' % (BASE_DIR,fname)
        newFile.download(path)
        add_file_to_active_task(update.message.chat_id,path)
    

def textMessage(update: Updater, context: CallbackContext):
    
    #response = 'Получил Ваше сообщение: ' + update.message.text + str(update.message.photo)
    #bot.send_message(chat_id=update.message.chat_id, text=response)
    is_reg = check_registration(update.message.from_user.username,update.message.chat_id,update.message.text)
    tsk = get_last_telegramm_task(update.message.chat_id)

    
    if tsk:
        #if tsk.is_done_from_telegramm == False:
        #    want_to_add_file_task(tsk,update.message.chat_id)
        #    return True
        if (
            len(update.message.text)>6 \
            and len(tsk.content)<2 \
            and tsk.subcategory \
            and tsk.category ) \
            or  ( len(update.message.text)>6 \
                and len(tsk.content)<2 \
                and not has_subcategory(tsk.category)\
                and tsk.category):

            finish_task(tsk,update.message.text,update.message.chat_id)
            return True
        elif is_reg:
            print('Comment')
            add_comment(tsk,update.message.text,update.message.chat_id)


        if len(tsk.content)<2 \
        and not has_subcategory(tsk.category) \
        and tsk.category \
        and not tsk.is_done_from_telegramm:
            send_what_content(update.message.chat_id)


def start(update: Updater, context: CallbackContext):
    print('got message!')
    is_reg = check_registration(update.message.from_user.username,update.message.chat_id,update.message.text)
    if is_reg:
        bot.send_message(update.message.chat_id, text="Выберите действие:", reply_markup=get_main_menu())
    return True
    username = update.message.from_user.username
    #logging.warning('dasdasdasdasdas')
    bot.send_message(update.message.chat_id, text="Подождите, идет настройка для логина %s." % username)
    try:
        profile = Profile.objects.get(telegram_login = username)
        profile.telegram_room = update.message.chat_id
        profile.save()
        bot.send_message(update.message.chat_id, text="Операция прошла успешно!\n Чтобы добавить новую заявку наберите команду /add.")        
    except:
        msg = "Логин %s не найден. Укажите его на <a href='%s/account/profile' >странице профайла </a>!" % (username, SITE_URL)
        send_html_message(update.message.chat_id,msg)

    send_help_message(update.message.chat_id)


def add(update: Updater, context: CallbackContext):
    print('add task!')
    add_new_task(update.message.chat_id)

def help(update: Updater, context: CallbackContext):
    send_help_message(update.message.chat_id)
    
def reg(update: Updater, context: CallbackContext):
    print('Registration') 
    username = update.message.from_user.username  
    check_registration(username,update.message.chat_id)


def list(update: Updater, context: CallbackContext):    
    send_html_message(update.message.chat_id, get_list_task_message(update.message.chat_id))

def activate(update: Updater, context: CallbackContext):    
    print('activation - '+str(context.args[0]))
    activate_task_by_id(context.args[0],update.message.chat_id)


def set_category_handler(update: Updater, context: CallbackContext):
    if update.callback_query.data == 'list_task':
        send_html_message(update.callback_query.message.chat_id, get_list_task_message(update.callback_query.message.chat_id))
    if update.callback_query.data == 'add_new_task':
        add_new_task(update.callback_query.message.chat_id)
    arr = update.callback_query.data.split('-')
    if len(arr)==2:
        if arr[1] == 'category':
            set_category(update.callback_query.message.chat_id,arr[0])
        if arr[1] == 'subcategory':
            set_sub_category(update.callback_query.message.chat_id, arr[0])

class Command(BaseCommand):
    def handle(self, *args, **option):
        print("Start bot %s" % TELEGRAMM_NAME)
        updater = Updater(token=TELEGRAMM_KEY, use_context=True)
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start', start)
        add_handler = CommandHandler('add', add)
        help_handler = CommandHandler('help', help, pass_args=True)
        reg_handler = CommandHandler('reg', reg)
        list_handler = CommandHandler('list', list, pass_args=True)
        activate_handler = CommandHandler('activate', activate, pass_args=True)
        text_message_handler = MessageHandler(Filters.text, textMessage)
        file_handler = MessageHandler(Filters.video | Filters.photo | Filters.document, fileHandler)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(add_handler)
        dispatcher.add_handler(text_message_handler)
        dispatcher.add_handler(file_handler)
        dispatcher.add_handler(help_handler)
        dispatcher.add_handler(reg_handler)
        dispatcher.add_handler(list_handler)
        dispatcher.add_handler(activate_handler)
        dispatcher.add_handler(telegram.ext.CallbackQueryHandler(set_category_handler))
        #dispatcher.add_handler(telegram.ext.CallbackQueryHandler(set_sub_category_handler))
        updater.start_polling()
       


