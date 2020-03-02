from django.db import models
from task.models import Task

def get_task_list(user,filter=None):
    if not filter:
        filter = 'all'
    if user.is_superuser:
        if filter == 'all':
            tasks = Task.objects.all().order_by('-id')
        else:
            tasks = Task.objects.filter(status=filter).order_by('-id')
    else:
        if filter == 'all':
            #print(Task.objects.all().query)
            tasks = Task.objects.filter(user=user).order_by('-id')
            #tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(user=user,status=filter).order_by('-id')
    return tasks