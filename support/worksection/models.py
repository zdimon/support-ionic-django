from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from django.contrib.auth.models import User

class WProject(models.Model):
    name = models.CharField(max_length=250, verbose_name=_(u'Заголовок'))
    page = models.CharField(max_length=250, verbose_name=_(u'Страница в системе worksection'), db_index=True, unique=True)
    status = models.CharField(max_length=50, verbose_name=_(u'Статус в системе worksection'))
    user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class WUser(models.Model):
    email = models.CharField(max_length=250, verbose_name=_(u'Email'), db_index=True, unique=True)
    name = models.CharField(max_length=250, verbose_name=_(u'Имя'))
    projects = models.ManyToManyField(WProject)

    def add_project(self,pr):
        if pr not in self.projects.all():
            print('Adddinnnnggg')
            self.projects.add(pr)



    @staticmethod
    def get_wuser_or_create(user_id):
        user = User.objects.get(pk=user_id)
        try:
            user = WUser.objects.get(user=user)
        except:
            user = User()
            user.user = user
            user.save()
        return user