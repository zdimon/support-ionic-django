"""support URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import index, get_script
from support.settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

urlpatterns = [
    path('', index, name='home'),
    path('admin/filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('account/', include('account.urls')),
    path('oauth/', include('social_django.urls', namespace='social')), 
    path('worksection/', include('worksection.urls')),
    path('task/', include('task.urls')),
    path('trello/', include('trelloapp.urls')),
    path('getScript/<str:site>/<str:lang>', get_script, name='get_script'),
    path('tinymce', include('tinymce.urls')),
    path('mobile_api/', include('mobile_api.urls'))
]


if DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()


    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

##if settings.DEBUG:
##    from django.conf.urls.static import static
##    urlpatterns += static('/pics/', document_root=/var/www/pictures/)
