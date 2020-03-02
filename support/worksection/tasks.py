from celery import task
from .lib.ws_api import save_projects_in_db, get_project_json, save_project_user_in_db

from worksection.lib.export_task import export_task_to_ws, export_comment_to_ws

@task()
def get_projects():
    data = get_project_json()
    #save_projects_in_db(data['data'])
    save_project_user_in_db(data['data'])
    export_task_to_ws

@task()
def task_export_task_to_ws(task):
    export_task_to_ws(task)
    print('Exporting task %s to ws' % task.id)


@task()
def task_export_comments_to_ws(comment):
    print('Exporting comment %s to ws' % comment.id)
    export_comment_to_ws(comment)