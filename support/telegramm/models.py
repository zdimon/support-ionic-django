from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
# Create your models here.

class ClientTelegramm(models.Model):
    name = models.CharField(verbose_name=_(u'Имя'), max_length=150, blank=True, null=True)
    domain = models.CharField(help_text='Без знаков http:// и слэшей в конце!', verbose_name=_(u'Доменное имя'), max_length=150, blank=True, null=True)
    login = models.CharField(verbose_name=_(u'Логин в telegramm'), max_length=150, blank=True, null=True, db_index=True)
    phone = models.CharField(verbose_name=_(u'Телефон'), max_length=150, blank=True, null=True)
    email = models.CharField(verbose_name=_(u'Email'), max_length=150, blank=True, null=True)
    chat_id = models.CharField(verbose_name=_(u'Чат ID'), max_length=150, blank=True, null=True)
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey ( settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, default=1)
    trello_board_name = models.CharField(max_length=250, verbose_name=_(u'Trello board'), default='', null=True, blank=True)