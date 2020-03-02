from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from main.models import Page
from django.contrib.auth.models import User
from .utils import *
import requests
from worksection.lib.ws_api import get_tasks_in_project_json, get_project_json, save_projects_in_db
from worksection.models import WProject

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('Request....load projects')
        data = get_project_json()
        save_projects_in_db(data['data'])



        
        