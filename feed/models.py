from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Post(models.Model):
    text=models.CharField(max_length=240)
    date=models.DateTimeField(auto_now=TRUE)

    def __str__(self):
        return self.text[0:100]