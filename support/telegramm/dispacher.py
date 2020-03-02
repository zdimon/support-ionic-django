from support.settings import TELEGRAMM_KEY, TELEGRAMM_NAME
import telegram
bot = telegram.Bot(token=TELEGRAMM_KEY)

def send_message(user,msg):
    try:
        bot.send_message(user.profile.telegram_room, text=msg,parse_mode=telegram.ParseMode.MARKDOWN)
    except:
        print('Error when sending to telegramm')

def send_html_message(chat_id,msg,reply_markup=None):
    try:
        bot.send_message(chat_id, text=msg,parse_mode=telegram.ParseMode.HTML,reply_markup=reply_markup)
    except Exception as e:
        print(str(e))
        print(msg)

def send_image(user,image):
    bot.send_photo(user.profile.telegram_room, photo=open(image, 'rb'))

def send_document(user,image):
    bot.send_document(user.profile.telegram_room, document=open(image, 'rb'))