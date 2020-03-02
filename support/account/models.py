from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.utils.translation import gettext as _
from telegramm.models import ClientTelegramm
import hashlib
import time

from worksection.models import WProject

class Client(models.Model):
    alias = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=150, unique=True, db_index=True)
    wproject =  models.ForeignKey(WProject, null=True, blank=True, on_delete=models.SET_NULL)
    trello_project_id =  models.CharField(null=True, blank=True, verbose_name=_(u'ID доски в trello'),max_length=250)
    trello_key =  models.CharField(null=True, blank=True, verbose_name=_(u'ключ в trello'),max_length=250, default="864189665a3e2f50c5e8a59461082c267024968d646f1dcecb7a6238cebbc7b4")
    trello_token =  models.CharField(null=True, blank=True,max_length=250, verbose_name=_(u'токен в trello'), default="1d980199101c6182074a15d587c4d008f00318337135dc7ce3f5c7ed784ffa03")
    template = models.CharField(max_length=100, blank=True, null=True, default='locotrade')

    contact_email =  models.CharField(null=True, blank=True,max_length=250)
    contact_phone =  models.CharField(null=True, blank=True,max_length=250)
    contact_name =  models.CharField(null=True, blank=True,max_length=250)
    contact_telegramm =  models.CharField(null=True, blank=True,max_length=250)

    user = models.ForeignKey ( settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_DEFAULT, default=1)

    sign = models.CharField(max_length=250, blank=True, null=True, default='')
    def set_sign(self):
        sign = hashlib.md5(str(time.time()).encode('UTF-8')).hexdigest()
        self.sign = sign
        #self.save()
        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_sign()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.alias)

    @staticmethod
    def get_client_by_host(host):
        #print(host)
        try:
            return Client.objects.get(alias=host)
        except:
            #create_client_if_not_exist(host)    
            return False

    @staticmethod
    def get_user(alias):
        try:
            return Client.objects.get(alias=alias).user    
        except:
            return None


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Customer'),
        (1, 'Admin'),
    )
    user = models.OneToOneField ( 
                                 settings.AUTH_USER_MODEL,\
                                 primary_key=True,\
                                 on_delete=models.CASCADE
                                )

    user_type = models.IntegerField(default=0, null=True, choices=USER_TYPES)
    name = models.CharField(max_length=200, blank=True, null=True, default='')
    is_support = models.BooleanField(default=False, verbose_name=_(u'суппорт'))
    client = models.ForeignKey (Client, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return "{}".format(self.user.username)
    class Meta:
        abstract = True



class CustomerProfile(models.Model):
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    class Meta:
        abstract = True


class Profile(BaseProfile, CustomerProfile):
    sign = models.CharField(max_length=250, blank=True, null=True, default='')
    def set_sign(self):
        sign = hashlib.md5(str(time.time()).encode('UTF-8')).hexdigest()
        self.sign = sign
        self.save()

    @staticmethod
    def get_user_by_chat_id(chat_id):
        try:
            pr = ClientTelegramm.objects.get(chat_id=chat_id)
        except:
            pr = Profile.objects.get(telegram_room=chat_id)
            
        #print(pr.user)
        return pr.user






class ClientChannel(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    key = models.CharField(max_length=250, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    is_new = models.BooleanField(default=False, verbose_name=_(u'новые задачи'))




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
    if not created:
        return
    # Create the profile object, only if it is newly created
    profile = Profile(user=instance)
    profile.save()
    profile.set_sign()
    



def create_client_if_not_exist(location):
    try:
        Client.objects.get(location=location)
    except:
        #import pdb; pdb.set_trace()
        
        cl = Client()
        cl.alias = 'locotrade'
        cl.location = location
        #cl.trello_project_id = '5c7912e07b9e8e3ca7008f6f'
        #cl.trello_key = 'c489233b2281ded1c28a07922ced5880'
        #cl.trello_token = '1d980199101c6182074a15d587c4d008f00318337135dc7ce3f5c7ed784ffa03'
        cl.save()


class PreAccount(models.Model):
    email = models.CharField(max_length=150, blank=True, null=True)
    telegram = models.CharField(max_length=250, blank=True, null=True)
    is_registered = models.BooleanField(default=False)
    client = models.ForeignKey (Client, on_delete=models.SET_NULL, blank=True, null=True)

class Client2User(models.Model):
    user = models.ForeignKey ( settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, default=1)
    client = models.ForeignKey (Client, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'client',)