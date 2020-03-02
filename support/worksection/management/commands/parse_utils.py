import requests
from bs4 import BeautifulSoup

def get_tasks_from_main(html):
    soup = BeautifulSoup(html, 'html.parser')
    #print(html)
    tbl_hot = soup.find('div',{'id': 'item_list'})
    tbl = tbl_hot.findAll('div', {'class': 'item'})
    for t in tbl:
        it = t.find('div',{'class': 'text'})
        link = it.find('a',{'class': 't'})
        print(link.text)
    #print(tbl)
