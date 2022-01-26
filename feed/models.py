from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from datetime import datetime    

# Create your models here.

class Post(models.Model):
    text=models.CharField(max_length=240)
    # image=ImageField()
    date=models.DateTimeField(auto_now=TRUE)
    author=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.text[0:100]



