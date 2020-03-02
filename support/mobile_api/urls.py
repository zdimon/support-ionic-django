from django.urls import path, include
from .views import *

urlpatterns = [
    path('settings', settings),
    path('task_list/<str:filter>', task_list),
    path('enter_client', enter_client),
    path('enter_task', enter_task),
    path('save_comment', save_comment),
    path('set_status', set_status),
    path('photo', photo),
    path('show_task/<int:task_id>', show_task),
    path('save_task', save_task),
]