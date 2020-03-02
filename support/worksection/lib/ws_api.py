from support.settings import WORKSECTION_KEY
import hashlib
import requests
import sys
import json
from worksection.models import WProject, WUser
from celery import task

def save_project_user_in_db(i):
    #for i in json:
    pr = WProject.objects.get(page=i['page'])
    try:
        u = WUser.objects.get(email=i['user_from']['email'])
        #pr = WProject.objects.get(page=i['page'])
        #u.add_project(p)
        print('Exist...%s' % i['user_from']['email'])
    except:
        u = WUser()
        u.email = i['user_from']['email']
        u.name = i['user_from']['name']
        u.save()
        #pr = WProject.objects.get(page=i['page'])
        print('Saving...%s' % i['user_from']['email'])
    u.add_project(pr)

    try:
        u = WUser.objects.get(email=i['user_to']['email'])
        #pr = WProject.objects.get(page=i['page'])
        #u.add_project(p)
        print('Exist...%s' % i['user_to']['email'])
    except:
        u = WUser()
        u.email = i['user_to']['email']
        u.name = i['user_to']['name']
        u.save()
        #pr = WProject.objects.get(page=i['page'])
        print('Saving...%s' % i['user_to']['email'])
    u.add_project(pr)



def save_projects_in_db(json):
    for i in json:
        if i['status'] == 'active':
            try:
                p = WProject.objects.get(page=i['page'])
                print('Exist...%s' % i['name'])
            except:
                p = WProject()
                try:
                    p.page = i['page']
                except:
                    import pdb; pdb.set_trace()
                p.name = i['name']
                p.status = i['status']
                p.save()
                print('Saving...%s' % i['name'])
                save_project_user_in_db(i)

def get_project_json():
    action = 'get_projects'
    key_str = '%s%s' % (action,WORKSECTION_KEY)
    hash = hashlib.md5(key_str.encode()).hexdigest()
    url = 'https://wezom.worksection.com/api/admin/?action=get_projects&hash=%s' % hash
    print(url)
    res = requests.get(url)
    #print(res.text)
    out = json.loads(res.text)
    return out
        

def get_tasks_in_project_json(prj):
    action = 'get_all_tasks'
    page = prj.page
    key_str = '%s%s' % (action,WORKSECTION_KEY)
    hash = hashlib.md5(key_str.encode()).hexdigest()
    url = 'https://wezom.worksection.com/api/admin/?action=get_all_tasks&hash=%s' % hash
    print(url)