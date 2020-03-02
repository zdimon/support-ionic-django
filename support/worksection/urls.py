from django.urls import path, include
from .views import *

urlpatterns = [
    path('get_hot_events', get_hot_events, name='get_hot_events'),
    path('get_content_task/<int:pk>', get_content_task, name='get_content_task'),
    path('idex', IndexView.as_view(), name='w_index'),
    path('projects', ProjectView.as_view(), name='w_projects'),
    path('import_projects', import_projects, name='w_import_projects'),

    path('import_projects_api', import_projects_api, name='import_projects_api'),

    path('export_task_to_ws/<int:id>', export_task_to_ws, name='export_task_to_ws'),
    path('export_task_to_trello/<int:id>', export_task_to_trello, name='export_task_to_trello'),


]