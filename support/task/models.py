from django.db import models
from django.utils.translation import gettext as _
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from telegramm.dispacher import send_message, send_image, send_document
from django.urls import reverse
from worksection.lib.utils import get_task_info
from support.settings import SITE_URL
from trelloapp.tasks import task_export_comment_to_trello, task_export_task_to_trello, task_export_file_to_trello
from worksection.tasks import task_export_comments_to_ws, task_export_task_to_ws
from account.models import Client
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name=_(u'Заголовок'))
    def __str__(self):
        return self.title
    
class SubCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name=_(u'Заголовок'))
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Task(models.Model):
    previous_status = None

    TYPE_CHOICES = (
    ("new", "В процессе рассмотрения"),
    ("inprocess", "В работе"),
    ("done", "Выполнен"),
)
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=150, verbose_name=_(u'Заголовок'))
    content = models.TextField(verbose_name=_(u'Содержание'))
    contacts = models.TextField(verbose_name=_(u'Контакты'))
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, verbose_name=_(u'Статус'), default='new', choices=TYPE_CHOICES)

    trello_board_name = models.CharField(max_length=250, verbose_name=_(u'Trello board'), default='', null=True, blank=True, db_index=True)

    telegramm_room = models.CharField(max_length=100, null=True, blank=True, verbose_name=_(u'telegramm chat_id'), default='')
    is_from_telegramm = models.BooleanField(default=False, verbose_name=_(u'Is from telegramm?'))
    is_done_from_telegramm = models.BooleanField(default=False, verbose_name=_(u'Is done from telegramm?'))
    is_active = models.BooleanField(default=False, verbose_name=_(u'Is active?'))
    source =  models.CharField(max_length=250, verbose_name=_(u'Источник'), default='')
    is_ws_exported = models.BooleanField(default=False, verbose_name=_(u'Is WS exported?'))
    ws_link = models.CharField(max_length=250, verbose_name=_(u'WS link'), default='', blank=True, null=True)
    is_trello_exported = models.BooleanField(default=False, verbose_name=_(u'Is WS exported?'))
    trello_link = models.CharField(max_length=250, null=True, blank=True, verbose_name=_(u'Trello link'), default='')
    trello_id = models.CharField(max_length=250, null=True, blank=True, verbose_name=_(u'Trello id'), default='', db_index=True)
    is_deleted = models.BooleanField(default=False, verbose_name=_(u'Is deleted?'))
    def __str__(self):
        return '%s (%s->%s)' % (self.title, self.category, self.subcategory)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    @property
    def category_str(self):
        if self.subcategory:
            return '%s -> %s' % (self.category, self.subcategory)
        else:
            return '%s' % self.category

    @property
    def get_status(self):
        if self.is_deleted == True:
            return 'Закрыто'
        else:
            return self.get_status_display()

    @property
    def get_last_comment(self):
        try:
            com = Comment.objects.filter(task=self).order_by('-id')[0]
            return 'Последний коментарий: <p><strong>%s</strong></p>' % com.content
        except:
            return ''        

    @property
    def w_link(self):
        return format_html('<a target=_blank href="%s">Worksection</a>' % self.ws_link)

    def get_absolute_url(self):
        return reverse("show_task", args=[self.pk])

    def get_ws_id(self):
        arr = self.ws_link.split('/')
        #print(arr)
        return arr[len(arr)-2]

    def get_trello_id(self):
        arr = self.trello_link.split('/')
        #print(arr)
        return arr[len(arr)-2]

    def set_title(self):
        wd = self.content.split(' ')
        self.title = self.title+' '.join(wd[0:5])+'...'
    
    def set_active(self):
        Task.objects.filter(user=self.user).update(is_active=False)
        self.is_active = True
        self.save()
        
    def export(self):
        #return True
        #task_export_task_to_ws.delay(self)
        task_export_task_to_trello.delay(self)

    @staticmethod
    def post_save(sender, **kwargs):
        instance = kwargs.get('instance')
        created = kwargs.get('created')
        if instance.previous_status != instance.status:
            msg = 'Задача "%s" изменен статус на "%s"' % (instance.title, instance.status)
            send_message(instance.user,msg)
        if created:
            get_task_info(instance)



    @staticmethod
    def remember_status(sender, **kwargs):
        instance = kwargs.get('instance')
        instance.previous_status = instance.status


post_save.connect(Task.post_save, sender=Task)
post_init.connect(Task.remember_status, sender=Task)


class Comment(models.Model):

    file = models.FileField(upload_to='files', null=True, blank=True)
    content = models.TextField(max_length=150, verbose_name=_(u'Содержание'), null=True, blank=True)
    author = models.TextField(max_length=250, verbose_name=_(u'Автор'), null=True, blank=True)
    avatar = models.TextField(max_length=250, verbose_name=_(u'Аватар'), null=True, blank=True)

    file_url = models.TextField(max_length=250, verbose_name=_(u'Ссылка на файл'), null=True, blank=True)
    file_url_orig = models.TextField(max_length=250, verbose_name=_(u'Ссылка на превью'), null=True, blank=True)

    task = models.ForeignKey(Task, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.SET_NULL)
    is_ws_exported = models.BooleanField(default=False, verbose_name=_(u'Is WS exported?'))
    ws_id = models.CharField(max_length=250, verbose_name=_(u'WS ID'), default='')
    is_trello_exported = models.BooleanField(default=False, verbose_name=_(u'Is trello exported?'))
    is_file = models.BooleanField(default=False, verbose_name=_(u'Is file?'))
    trello_id = models.CharField(max_length=250, null=True, blank=True, verbose_name=_(u'Trello ID'), default='')
    is_support = models.BooleanField(default=False, verbose_name=_(u'суппорт'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)    
    def is_image(self):
        if self.file:
            if (self.file.name.endswith('jpeg') or \
                self.file.name.endswith('png') or \
                self.file.name.endswith('jpg') or \
                self.file.name.endswith('gif') \
            ):
                return True
            return False
        return False

    def get_file_uri(self):
        if self.file:
            return "%s%s" % (SITE_URL,self.file.url)
        if self.file_url:
            return self.file_url

    def get_file_url(self):
        if self.file:
            if self.is_image():
                return format_html('<img src="%s%s" />' % (SITE_URL,self.file.url))
            else:
                return format_html('<a target=_blank href="%s" >Ссылка на файл документа</a>' % self.get_file_uri())
        if self.file_url:
            return format_html('<a target=_blank href="%s" >Ссылка на файл документа</a>' % self.get_file_uri())  
        return ''
    '''
    @staticmethod
    def post_save(sender, **kwargs):
        created = kwargs.get('created')
        instance = kwargs.get('instance')
        #import pdb; pdb.set_trace()
        if created:
            if instance.file:
                msg = 'Задача #%s "%s" добавлен файл.' % (instance.pk,instance.task.title)
                if instance.user:
                    send_message(instance.user,msg)
                    if instance.is_image():
                        send_image(instance.user,instance.file.path)
                    else:
                        send_document(instance.user,instance.file.path)
            elif len(instance.content)>2:
                if instance.user:
                    msg = 'Задача "%s" добавлен комментарий: \n *%s*' % (instance.task.title, instance.content)
                    send_message(instance.user,msg)
                #if instance.task.is_trello_exported:
                #    task_export_comment_to_trello.delay(instance)
                #    instance.is_trello_exported = True
                #    instance.save()
                #if instance.file:
                #    task_export_file_to_trello(instance)
                if instance.task.is_ws_exported:
                    task_export_comments_to_ws.delay(instance)
                
    '''

    def __str__(self):
        if self.content:
            return self.content
        else:
            return 'file'


#post_save.connect(Comment.post_save, sender=Comment)




class Log(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
