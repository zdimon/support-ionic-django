import requests
from bs4 import BeautifulSoup
import sys
import re

def check_is_login_form(html):
    soup = BeautifulSoup(html, 'html.parser')
    if soup.find('input',{'name': 'email'}):
        return True
    else:
        return False



def save_log(html):
    with open('log.txt', 'w') as f:
        f.write(html)


def get_more_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    link = soup.find('div',{'class': 'more'})
    try:
        result = re.search('&mda=(.*)&cp4=5', link['onclick'])
    except:
        print(html)

    
    return 'https://wezom.worksection.com/?action=hot_events&mda=%s&cp4=5' % result.group(1)



def parse_tasks_from_main(html):
    save_log(html)
    soup = BeautifulSoup(html, 'html.parser')
    out = []
    
    tbl_hot = soup.find('div',{'id': 'item_list'})
    tbl = tbl_hot.findAll('div', {'class': 'item'})
    for t in tbl:
        it = t.find('div',{'class': 'text'})
        link = it.find('a',{'class': 't'})
        desc = ''
        for sp in it.findAll('span'):
            desc = desc+' '+sp.text
        out.append({
            'url': link['href'],
            'title': link.text,
            'desc': desc
        })
        #print(link.text)
    return out
    
