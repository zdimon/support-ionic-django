from django.core.management.base import BaseCommand, CommandError
import os
from account.models import Profile
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext
import logging
from support.settings import TELEGRAMM_KEY
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
    

class Command(BaseCommand):
    def handle(self, *args, **option):
        from telegramm.models import ClientTelegramm
        print("Deleting Telegram clients")
        ClientTelegramm.objects.all().delete()