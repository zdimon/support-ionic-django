from task.models import Comment

def get_status_str(status):
    if status=='new':
        return 'paper-plane'
    elif status=='inprocess':
        return 'build'
    elif status=='new':
        return 'paper-plane'
    elif status=='done':
        return 'boat'
    else:
        return ''

def serialize_task(task):
    out = {
            "id": task.id,
            "title": task.title,
            "content": task.content,
            "status": task.status,
            "status_icon": get_status_str(task.status),
            "author": task.user.profile.name,
            "comments": []
    }
    for c in Comment.objects.filter(task=task).order_by('id'):
        if c.file:
            file = c.get_file_uri()
        else:
            file = None
        out['comments'].append(
            {
                'content': c.content,
                'is_image': c.is_image(),
                'file': file,
                'link': c.get_file_url(),
                'user': c.user.profile.name
            }
        )
    return out

def serialize_task_list(tasks):
    out = []
    for i in tasks:
        out.append(serialize_task(i))
    return out