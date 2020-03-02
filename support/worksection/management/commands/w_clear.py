from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from main.models import Page
from django.contrib.auth.models import User
from .utils import *
import requests
from worksection.lib.ws_api import get_tasks_in_project_json
from worksection.models import WProject, WUser

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Clearing...')
        WUser.objects.all().delete()
        WProject.objects.all().delete()
        print('Finished...')


        
        