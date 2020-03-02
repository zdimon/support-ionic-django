from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models

class Page(models.Model):
    title = models.CharField(max_length=150, verbose_name=_(u'Заголовок'))
    content = models.TextField(verbose_name=_(u'Содержание'))
    name_slug = models.CharField(max_length=150, verbose_name=_(u'Алиас'))
    meta_title = models.CharField(max_length=150, verbose_name=_(u'Мета-заголовок'))
    meta_keywords = models.CharField(max_length=250, verbose_name=_(u'Мета-словосочитания'))
    meta_description = models.CharField(max_length=250, verbose_name=_(u'Мета-описание'))

    def __unicode__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('show_page', kwargs={'pk': self.pk})

class Digest(models.Model):
    title = models.CharField(max_length=250, verbose_name=_(u'Заголовок'))
    content = tinymce_models.HTMLField()
    is_published = models.BooleanField(default=False, verbose_name=_(u'Опубликовано?'))
    is_new = models.BooleanField(default=True, verbose_name=_(u'Новый?'))
