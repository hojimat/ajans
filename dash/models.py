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
	birth_date = models.DateField(blank=True)
	###########################################
	imagedir = models.TextField(max_length=500, blank=True)
	videodir = models.TextField(max_length=500, blank=True)
	ad = models.CharField(max_length=50, blank=False, default=0)
	soyad = models.CharField(max_length=50, blank=False, default=0)
	TCno = models.CharField(max_length=50, blank=False, default=0)
	baba = models.CharField(max_length=50, blank=True)
	gun	= models.IntegerField(default=0, blank=True)
	ay = models.CharField(max_length=15, blank=True)
	yil = models.IntegerField(default=0, blank=False)
	kayitgun = models.IntegerField(default=0, blank=True)
	kayitay = models.CharField(max_length=15, blank=True)
	kayityil = models.IntegerField(default=0, blank=True)
	tel1 = models.CharField(max_length=45, blank=True)
	bilgi1= models.CharField(max_length=45, blank=True)
	tel2 = models.CharField(max_length=45, blank=True)
	bilgi2= models.CharField(max_length=45, blank=True)
	tel3 = models.CharField(max_length=45, blank=True)
	bilgi3= models.CharField(max_length=45, blank=True)
	tel4 = models.CharField(max_length=45, blank=True)
	bilgi4= models.CharField(max_length=45, blank=True)
	tel5 = models.CharField(max_length=45, blank=True)
	bilgi5= models.CharField(max_length=45, blank=True)
	mail = models.CharField(max_length=45, blank=True)
	ulke = models.CharField(max_length=45, blank=True)
	il = models.CharField(max_length=45, blank=True)
	ilce = models.CharField(max_length=45, blank=True)
	adres = models.TextField(max_length=500, blank=True)
	bay = models.IntegerField(default=0, blank=False)
	bayan = models.IntegerField(default=0, blank=False)
	ucuncucins = models.IntegerField(default=0, blank=False)
	oryantel = models.IntegerField(default=0, blank=True)
	tbay = models.IntegerField(default=0, blank=True)
	tbayan = models.IntegerField(default=0, blank=True)
	muzisyen = models.IntegerField(default=0, blank=True)
	ikiz = models.IntegerField(default=0, blank=True)
	ybay = models.IntegerField(default=0, blank=True)
	ybayan = models.IntegerField(default=0, blank=True)
	ekstra = models.IntegerField(default=0, blank=True)
	cuce = models.IntegerField(default=0, blank=True)
	mbay = models.IntegerField(default=0, blank=True)
	mbayan = models.IntegerField(default=0, blank=True)
	elcasti = models.IntegerField(default=0, blank=True)
	dovmeli = models.IntegerField(default=0, blank=True)
	boy = models.IntegerField(default=0, blank=True)
	kilo = models.IntegerField(default=0, blank=True)
	beden = models.IntegerField(default=0, blank=True)
	ayak = models.IntegerField(default=0, blank=True)
	goz = models.CharField(max_length=15, blank=True)
	ozellik = models.TextField(max_length=5000, blank=True)
	pazartesi = models.IntegerField(default=0, blank=True)
	sali = models.IntegerField(default=0, blank=True)
	carsamba = models.IntegerField(default=0, blank=True)
	persembe = models.IntegerField(default=0, blank=True)
	cuma = models.IntegerField(default=0, blank=True)
	cumartesi = models.IntegerField(default=0, blank=True)
	pazar = models.IntegerField(default=0, blank=True)
	emekli = models.TextField(max_length=5000, blank=True)
	pasaport = models.IntegerField(default=0, blank=True)
	sgk = models.IntegerField(default=0, blank=True)
	protokol = models.IntegerField(default=0, blank=True)
	d = models.IntegerField(default=0, blank=True)
	r = models.IntegerField(default=0, blank=True)
	df = models.IntegerField(default=0, blank=True)
	dans = models.IntegerField(default=0, blank=True)
	solist = models.IntegerField(default=0, blank=True)
	ozeltip = models.IntegerField(default=0, blank=True)
	dublor = models.IntegerField(default=0, blank=True)
	dublaj = models.IntegerField(default=0, blank=True)
	engelli = models.IntegerField(default=0, blank=True)
	gorme = models.IntegerField(default=0, blank=True)
	isitme = models.IntegerField(default=0, blank=True)
	kekeme = models.IntegerField(default=0, blank=True)
	down = models.IntegerField(default=0, blank=True)
	sacsekli = models.CharField(max_length=45, blank=True)
	sacrengi = models.CharField(max_length=100, blank=True)
	tenrengi = models.CharField(max_length=45, blank=True)
	incelendi= models.IntegerField(default=0, blank=True)
	otizm = models.IntegerField(default=0, blank=True)
	TCStatus = models.IntegerField(default=0, blank=True)

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

