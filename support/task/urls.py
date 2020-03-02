from django.urls import path, include
from .views import *

urlpatterns = [
    path('edit_task/<int:pk>', edit_task, name='edit_task'),
    path('show_task/<int:pk>', show_task, name='show_task'),


    path('getTaskList/<str:site>/<str:lang>/<str:status>', get_task_list, name='get_task_list'),
    path('getTaskForm/<str:site>/<str:lang>', get_task_form, name='get_task_form'),
    path('getTask/<str:site>/<str:lang>/<int:id>', show_task_locotrade),
    path('saveTask', save_task, name='save_task'),
    path('saveComment', save_comment, name='save_comment'),
    path('saveFile', save_file),
    path('updateTask', update_task),
    path('delTask/<str:site>/<int:id>', del_task),
    path('getTaskComment/<str:site>/<str:lang>/<int:id>', get_task_comment),
    path('getDigest/<str:site>/<str:lang>', get_digest),
    path('manageTask/<int:id>/<int:user_id>', manage_task),
]