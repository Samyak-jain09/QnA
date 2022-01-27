from django.urls import re_path
from django.contrib import admin
from .views import (searchposts)

app_name='searchposts'

urlpatterns = [
     re_path(r'^$', searchposts, name='searchposts'),

]