from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# User Profile class
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



# DATABASE STRUCTURE

    
# Real Estate Class
# CITIES = ("", "")
# HEATING = ("", "")
# RE_TYPE = ("konut", "isyeri", "arsa", "bina")
class RealEstate(models.Model):
    re_type = models.CharField(max_length=30)#, choices=RE_TYPE
    price = models.IntegerField()
    year = models.IntegerField()
    site_mi = models.BooleanField()
    area = models.IntegerField()
    oda_no = models.IntegerField()
    salon_no = models.IntegerField()
    banyo_no = models.IntegerField()
    heating = models.CharField(max_length=30) #, choices=HEATING)
    #foreign keys:
    owner_id = models.IntegerField()
    campaign_id = models.IntegerField()


# CURRENT_STATUSES = ("", "")     
# Campaign Class
class Campaign(models.Model):
    duedate = models.DateField()
    shareno = models.IntegerField()
    current_status = models.CharField(max_length=30) #, choices=CURRENT_STATUSES)
    #foreign_keys
    users_invested_id = models.IntegerField()
    real_estates_id = models.IntegerField()
    class Meta:
        pass



###############
## DASHBOARD ##
###############

# Message Class
class Message(models.Model):
    user_id = models.IntegerField(blank=False)
    sender = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    unread = models.BooleanField(default=True)
    time_sent = models.DateTimeField(editable=False, blank=False)

# Notification Class
class Notification(models.Model):
    user_id = models.IntegerField(blank=False)
    subject = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    unread = models.BooleanField(default=True)
    time_notified = models.DateTimeField(editable=False, blank=False)

