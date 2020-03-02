from django.urls import path, include
from .views import *

urlpatterns = [
    path('alogin', alogin, name='alogin'),
    path('login', login, name='login'),
    path('logout', logoutme, name='logout'),
    path('registration', registration, name='registration'),
    path('registration/done', registration_done, name='registration_done'),
    path('test_telegramm', test_telegramm, name='test_telegramm'),
    path('worksection', worksection, name='worksection'),
    path('import_worksection', import_worksection, name='import_worksection'),
    path('profile', profile, name='profile')
]