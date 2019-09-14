from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class NewsFeeds(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True, )
    message = models.CharField(max_length=2000, blank=True, null=True,)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    sub = models.CharField(max_length=50, null=True)

class reminder(models.Model):
    date = models.DateField(blank=True, null=True)
    event = models.CharField(max_length=100, blank=True, null=True)

Department = (
    ('BCA', 'BCA'),
    ('BBA', 'BBA'),
    ('BCOM', 'BCOM'),
)
Semester = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dept = models.CharField(max_length=30, blank=False, choices=Department)
    sem = models.CharField(max_length=30, blank=False, choices=Semester)
    is_online = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
