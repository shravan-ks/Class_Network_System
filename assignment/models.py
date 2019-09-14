from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class assignment(models.Model):
    SEM = (
        ('6', '6'),
        ('4', '4'),
        ('2', '2'),
    )
    DEPT = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('BCOM','BCOM'),
    )
    dept = models.CharField(max_length=3, choices=DEPT, blank=False,)
    sem = models.CharField(max_length=10, choices=SEM, blank=False,)
    Paper = models.CharField(max_length=30, blank=False,)
    title = models.CharField(max_length=100)
    sub = models.CharField(max_length=400)
    body = models.TextField(max_length=5000, blank=True, null=True,)
    Attachments = models.FileField(upload_to='files/', blank=True, null=True,)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    From = models.CharField(max_length=50,blank=True,null=True)

class AssignmentAns(models.Model):
    Paper = models.CharField(max_length=30, blank=False, )
    Title = models.CharField(max_length=100)
    sub = models.CharField(max_length=400)
    Solution = models.TextField(max_length=5000)
    Attachment = models.FileField(upload_to='files/', blank=True, null=True, )
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User)