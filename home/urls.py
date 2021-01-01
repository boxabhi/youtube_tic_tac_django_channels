
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    
    path('' , home , name="home"),
    path('play/<room_code>' , play , name="play"),
   
]
