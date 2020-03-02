from django.shortcuts import render, redirect
from .lib.utils import *
from .lib.parse_utils import *
from django.http import HttpResponse
from django.contrib import messages
from .models import WProject
from task.models import Task
from django.views.generic import TemplateView, ListView

from worksection.tasks import task_export_task_to_ws
from trelloapp.tasks import task_export_task_to_trello


def export_task_to_trello(request,id):
    task = Task.objects.get(pk=id)
    task_export_task_to_trello.delay(task)
    #export_to_trello(task,request.user)
    messages.warning(request, 'Экспорт в trello завершен.')
    return redirect('show_task', id)


def export_task_to_ws(request,id):
    task = Task.objects.get(pk=id)
    #export_to_ws(task,request.user)
    task_export_task_to_ws.delay(task)
    messages.warning(request, 'Экспорт в worksection запущен.')
    return redirect('show_task', id)

class IndexView(TemplateView):
    template_name = "worksection/index.html"


class ProjectView(ListView):
    template_name = "worksection/project_list.html"
    model = WProject


def import_projects(requests):
    if not check_login(request.user.profile):
        messages.warning(request, 'Неправильный логин или пароль!')
        return redirect('profile')
    html = get_main_page(request.user)
    return HttpResponse('Ok')

def get_hot_events(request):
    if not check_login(request.user.profile):
        messages.warning(request, 'Неправильный логин или пароль!')
        return redirect('profile')
    html = get_main_page(request.user)
    messages.success(request, 'Импорт данных завершен!')
    return redirect('home')


def get_content_task(request,pk):
    html = get_main(request.user)
    messages.success(request, 'Забор данных!')
    return redirect('home')


def import_projects_api(request):
    from .tasks import get_projects
    messages.success(request, 'Забор данных!')
    get_projects.delay()
    #get_projects()
    return redirect('home')