from .models import Task, Category, SubCategory, Comment

def create_task(title,content,user):
    print(user)
    '''
    site = request.POST.get('source')
    user = Client.get_user(site)
    print(site)
    client = Client.objects.get(location=request.POST.get('source'))
    client.contact_email = request.POST.get('email')
    client.contact_phone = request.POST.get('phone')
    client.save()

    t = Task()
    t.title = request.POST.get('title')
    t.content = request.POST.get('content')
    t.contacts = '\n email: %s' % request.POST.get('email')
    t.content = nl2br(t.content)
    if len(request.POST.get('phone'))>2:
        t.contacts = t.contacts + '\n тел: %s' % request.POST.get('phone')
    t.category_id = request.POST.get('category')
    t.subcategory_id = request.POST.get('subcategory')
    t.source = client
    t.user = user
    t.save()
    t.export()
    '''

