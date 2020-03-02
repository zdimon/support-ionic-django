from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from main.models import Page
from django.contrib.auth.models import User
from task.models import Task, Comment
#import redis

#redis_client = redis.Redis(host='localhost', port=6379, db=0)

from task.tornado_lib import ws_update_task

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Testing tornado')
        #redis_client.publish("support-channel", 'support-channel')
        ws_update_task(10)
        