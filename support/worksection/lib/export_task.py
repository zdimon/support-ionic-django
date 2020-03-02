import requests
from support.settings import WORKSECTION_KEY, WORKSECTION_PROJECT_PAGE, WORKSECTION_PROJECT_ID
import hashlib
import json


def export_task_to_ws(task):

    print('Exporting...ws')
    action = 'post_task'
    key_str = '%s%s%s' % (WORKSECTION_PROJECT_PAGE,action,WORKSECTION_KEY)
    hash = hashlib.md5(key_str.encode()).hexdigest()
    url = 'https://wezom.worksection.com/api/admin/?action=post_task&page=%s&email_user_from=%s&email_user_to=%s&title=%s&hash=%s&text=%s' % (WORKSECTION_PROJECT_PAGE,task.user.profile.w_login, task.user.profile.w_login,task.title,hash,task.content)
    r = requests.get(url)
    rez = json.loads(r.text)
    task.is_ws_exported = True
    task.ws_link = rez['url']
    task.save()
    print(r.text)

def export_comment_to_ws(comment):
    '''
        https://your-domain.com/api/admin/?action=post_comment&page=/project/ID_PROJECT/ID_TASK/&email_user_from=USER_EMAIL&text=TEXT&hash=HASH
    '''
    if not comment.is_ws_exported:
        action = 'post_comment'
        page = WORKSECTION_PROJECT_PAGE+comment.task.get_ws_id()+'/'
        key_str = '%s%s%s' % (page,action,WORKSECTION_KEY)
        hash = hashlib.md5(key_str.encode()).hexdigest()
        url = 'https://wezom.worksection.com/api/admin/?action=post_comment&page=/project/%s/%s/&email_user_from=%s&text=%s&hash=%s' % \
        (WORKSECTION_PROJECT_ID,comment.task.get_ws_id(),comment.task.user.profile.w_login,comment.content,hash)
        r = requests.get(url)
        rez = json.loads(r.text)
        print(rez)
        comment.is_ws_exported = True
        comment.save()
        #print('task id %s' % comment.task.get_ws_id())



   