from celery import task
from worksection.lib.export_task import export_task_to_ws
from .export_trello import export_task_to_trello, export_comment_to_trello, export_file_to_trello

@task()
def task_export_task_to_trello(task):
    export_task_to_trello(task)
    

@task()
def task_export_comment_to_trello(comment):
    export_comment_to_trello(comment)

@task()
def task_export_file_to_trello(comment):
    export_file_to_trello(comment)