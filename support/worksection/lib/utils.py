import requests
from bs4 import BeautifulSoup
from .parse_utils import *
from task.models import *
import sys

def get_mda():    
    url = 'https://wezom.worksection.com/login/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    input = soup.find("input", {"name":"mda"})
    return input['value']


def get_usid(login,password):
    session = requests.Session()
    url = 'https://wezom.worksection.com/login/'

    data = {
        'email': login,
        'password': password,
        'save_login': 1,
        'action': 'logon',
        'mda': get_mda(),
        'chk': 'frm_chk'
    }

    r = session.post(url,data=data,allow_redirects=False)
    return session.cookies.get_dict()['usid']



def check_login(user):
    #if not  user.w_uid:
    print("Checking user")
    session = requests.Session()
    url = 'https://wezom.worksection.com/login/'
    mda = get_mda()
    user.w_mda = mda
    data = {
        'email': user.w_login,
        'password': user.w_password,
        'save_login': 1,
        'action': 'logon',
        'mda': mda,
        'chk': 'frm_chk'
    }
    res = session.post(url,data=data,allow_redirects=True)
    #import pdb; pdb.set_trace()
    if check_is_login_form(res.text):
        return False
        #print(r.text)
        #sys.exit()
    res = session.cookies.get_dict()
    try:
        user.w_uid = res['usid']
        user.save()
    except:
        pass
    return True
    #print(res)


def save_task_in_db(json,user):
    from task.models import Task
    for i in json:
        try:
            Task.objects.get(w_url=i['url'])
        except:
            print('Saving')
            t = Task()
            t.title = i['title']
            t.content = i['desc']
            t.w_desc = i['desc']
            t.w_url = i['url']
            t.user = user
            t.save()


def save_hot_tasks(r):
    url = get_more_link(r.text)
    r = requests.get(url, cookies=cookies)
    result = parse_tasks_from_main(r.text)
    save_task_in_db(result,user)
    return result

def get_main_page(user):
        cookies = {
            'usid': user.profile.w_uid   
        }
        url = 'https://wezom.worksection.com/'
        r = requests.get(url, cookies=cookies)
        return save_hot_tasks(r.text)


def get_task_info(task):
    print('Getting info')