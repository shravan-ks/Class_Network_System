from django.contrib.auth.models import User
from django.db import models



# Create your models here.
from core.models import Profile


class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True,)
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.message

class classroom(models.Model):
    sem = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    sub = models.CharField(max_length=255)
