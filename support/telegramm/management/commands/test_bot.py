from django.core.management.base import BaseCommand, CommandError
import os
from main.models import Setting
from account.models import Profile
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext
import logging
from support.settings import TELEGRAMM_KEY
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    
bot = telegram.Bot(token=TELEGRAMM_KEY)

def start(update: Updater, context: CallbackContext):
    print('message!!!')
    username = update.message.from_user.username
    #logging.warning('dasdasdasdasdas')
    bot.send_message(update.message.chat_id, text="Подождите, идет настройка для логина %s." % username)
    try:
        profile = Profile.objects.get(telegram_login = username)
        profile.telegram_room = update.message.chat_id
        profile.save()
        bot.send_message(update.message.chat_id, text="Операция прошла успешно!")        
    except:
        bot.send_message(update.message.chat_id, text="Такой логин не найден в базе. Укажите его на странице профайла!")
    #bot.send_message(update.message.chat_id, text="I`m WEZOM bot, Initialisation... chat id %s" % update.message.chat_id)
    #print('message!!!')
    print(update.message.from_user.username)


class Command(BaseCommand):
    def handle(self, *args, **option):
        #setting = Setting.objects.get(alias='telegramm_bot_key')
        print("Start testing bot ")
        #bot = telegram.Bot(token=setting.value)
        updater = Updater(token=TELEGRAMM_KEY, use_context=True)
        dispatcher = updater.dispatcher
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)
        updater.start_polling()
        #start(bot,updater)
        #print(bot.get_me())
       


