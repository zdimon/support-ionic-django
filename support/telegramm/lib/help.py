import telegram
from task.models import Task
from support.settings import TELEGRAMM_KEY, TELEGRAMM_NAME, BASE_DIR
from telegramm.lib.messages import get_help_message

bot = telegram.Bot(token=TELEGRAMM_KEY)





def get_task(id):
    try:
        t = Task.objects.get(pk=id)
    except:
        t = False
    return t



def send_help_message(chat_id):
    #path = '%s/telegramm/static/image/w.jpg' % BASE_DIR
    #bot.send_photo(chat_id, photo=open(path, 'rb'))
    bot.send_message(chat_id, text=get_help_message(), parse_mode=telegram.ParseMode.MARKDOWN)