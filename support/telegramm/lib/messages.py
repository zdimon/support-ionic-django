from support.settings import TELEGRAMM_KEY, TELEGRAMM_NAME, SITE_URL, MOBILE_URL
from account.models import Profile
from task.models import Task
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def build_menu(buttons,n_cols):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    return menu

def get_help_message():
    msg_help = ''' *Команды бота:*
    */help* - помощь. Можно использовать с параметром (номер заявки).
    */list* - список последних 5 заявок
    */add* - добавить заявку
    */activate \[номер]* - активировать заявку
    '''
    return msg_help

def get_new_task_message(tsk):
    mobi_url = '%s/settings/login/%s/%s/task' % (MOBILE_URL,tsk.user.profile.sign,tsk.id)
    msg = 'Спасибо! Номер заявки "%s", статус: %s.' % (tsk.id, tsk.status)
    msg += '\n Чтобы отслеживать заявку на сайте нажмите на <a href="%s"> ссылку </a>. %s' % (mobi_url,mobi_url)

    msg += '\n Эта заявка является <strong style="color: red">ЕДИНСТВЕННО</strong> активной, вы можете добавить файл (не более 32М!) или комментарий.'
    #msg += '\n Чтобы добавить новую заявку напишите команду /add.'
    #msg += '\n Чтобы вывести последние заявки напишите команду /list.'
    #msg += '\n Чтобы активировать другую заявку напишите команду /activate \[номер заявки].'
    print(msg)
    return msg
    
def get_want_file_message():
    msg = 'Хотите добавить файл к заявке?'
    return msg


def get_list_task_message(chat_id, limit=5):
    user = Profile.get_user_by_chat_id(chat_id)
    items = Task.objects.filter(user=user).order_by('-is_active', 'id')[0:limit]
    if len(items)==0:
        return 'У вас нет заявок.'
    out = ''
    for t in items:
        if t.is_active:
            out += '\n <strong>#%s %s: %s</strong>' % (t.id,t.title, t.get_status)
        else:
            out += '\n #%s %s: %s' % (t.id,t.title, t.get_status)
    return out


def get_activate_task_message(chat_id, limit=5):
    user = Profile.get_user_by_chat_id(chat_id)
    out = ''
    for t in Task.objects.filter(user=user).order_by('-is_active', 'id')[0:limit]:
        if t.is_active:
            out += '\n <strong>#%s %s</strong>' % (t.id,t)
        else:
            out += '\n #%s %s' % (t.id,t)
    return out


def get_add_file_message():
    return 'Файл успешно добавлен!'


def get_main_menu(tsk=None):
    button_list = []
    if tsk:
        mobi_url = '%s/settings/login/%s/%s/task' % (MOBILE_URL,tsk.user.profile.sign,tsk.id)
    #try:
    #    button_list.append(InlineKeyboardButton('Просмотр задачи', url=mobi_url))
    #except:
    #    pass
    button_list.append(InlineKeyboardButton('Новая задача', callback_data='add_new_task'))
    button_list.append(InlineKeyboardButton('Список задач', callback_data='list_task'))
    #button_list.append(InlineKeyboardButton('Активная задача', callback_data='active_task'))
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))    
    return reply_markup



def get_change_status_message(task):
    msg = 'Статус заявки №%s "%s" изменен на "%s"' % (task.id, task.title, task.status)
    return msg

