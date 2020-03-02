import requests
from bs4 import BeautifulSoup
from .parse_utils import *

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

def get_main(uid):
        cookies = {
            'usid': uid
        }
        url = 'https://wezom.worksection.com/'
        url = 'https://wezom.worksection.com/?action=hot_events&mda=3e2deaf82a7ef654694735b43be0e5d1&cp4=5'
        r = requests.get(url, cookies=cookies)
        get_tasks_from_main(r.text)