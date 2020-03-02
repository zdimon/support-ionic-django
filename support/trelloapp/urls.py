from django.urls import path, include
from .views import *

urlpatterns = [
    path('hook', get_hook)
   
]