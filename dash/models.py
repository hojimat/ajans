from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class Actor(models.Model):

	# PRIVATE FIELDS
	ad = models.CharField(max_length=50, blank=False, default=0)
	soyad = models.CharField(max_length=50, blank=False, default=0)
	TCno = models.CharField(max_length=50, blank=False, default=0)
	baba = models.CharField(max_length=50, blank=True)
	gun	= models.IntegerField(default=1, blank=True)
	ay = models.CharField(max_length=15, blank=True)
	yil = models.IntegerField(default=1990, blank=False)
	kayitgun = models.IntegerField(default=1, blank=True)
	kayitay = models.CharField(max_length=15, blank=True)
	kayityil = models.IntegerField(default=2019, blank=True)
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
	adres = models.TextField(max_length=500, blank=True)
	
	
	# PUBLIC FIELDS
	image = models.ImageField(upload_to="images", blank=True)
	video = models.FileField(upload_to="videos", blank=True)
	imagedir = models.CharField(max_length=100, blank=True)
	videodir = models.CharField(max_length=100, blank=True)
	ulke = models.CharField(max_length=45, blank=True)
	il = models.CharField(max_length=45, blank=True)
	ilce = models.CharField(max_length=45, blank=True)
	bay = models.BooleanField(default=False, blank=False)
	bayan = models.BooleanField(default=False, blank=False)
	ucuncucins = models.BooleanField(default=False, blank=False)
	oryantel = models.BooleanField(default=False, blank=False)
	tbay = models.BooleanField(default=False, blank=False)
	tbayan = models.BooleanField(default=False, blank=False)
	muzisyen = models.BooleanField(default=False, blank=False)
	ikiz = models.BooleanField(default=False, blank=False)
	ybay = models.BooleanField(default=False, blank=False)
	ybayan = models.BooleanField(default=False, blank=False)
	ekstra = models.BooleanField(default=False, blank=False)
	cuce = models.BooleanField(default=False, blank=False)
	mbay = models.BooleanField(default=False, blank=False)
	mbayan = models.BooleanField(default=False, blank=False)
	elcasti = models.BooleanField(default=False, blank=False)
	dovmeli = models.BooleanField(default=False, blank=False)
	boy = models.IntegerField(default=0, blank=True)
	kilo = models.IntegerField(default=0, blank=True)
	beden = models.IntegerField(default=0, blank=True)
	ayak = models.IntegerField(default=0, blank=True)
	goz = models.CharField(max_length=15, blank=True)
	ozellik = models.TextField(max_length=5000, blank=True)
	pazartesi = models.BooleanField(default=False, blank=False)
	sali = models.BooleanField(default=False, blank=False)
	carsamba = models.BooleanField(default=False, blank=False)
	persembe = models.BooleanField(default=False, blank=False)
	cuma = models.BooleanField(default=False, blank=False)
	cumartesi = models.BooleanField(default=False, blank=False)
	pazar = models.BooleanField(default=False, blank=False)
	emekli = models.TextField(max_length=5000, blank=True)
	pasaport = models.IntegerField(default=0, blank=True)
	sgk = models.BooleanField(default=False, blank=False)
	protokol = models.IntegerField(default=0, blank=True)
	d = models.IntegerField(default=0, blank=True)
	r = models.IntegerField(default=0, blank=True)
	df = models.IntegerField(default=0, blank=True)
	dans = models.BooleanField(default=False, blank=False)
	solist = models.BooleanField(default=False, blank=False)
	ozeltip = models.BooleanField(default=False, blank=False)
	dublor = models.BooleanField(default=False, blank=False)
	dublaj = models.BooleanField(default=False, blank=False)
	engelli = models.BooleanField(default=False, blank=False)
	gorme = models.BooleanField(default=False, blank=False)
	isitme = models.BooleanField(default=False, blank=False)
	kekeme = models.BooleanField(default=False, blank=False)
	down = models.BooleanField(default=False, blank=False)
	sacsekli = models.CharField(max_length=45, blank=True)
	sacrengi = models.CharField(max_length=100, blank=True)
	tenrengi = models.CharField(max_length=45, blank=True)
	incelendi= models.BooleanField(default=False, blank=False)
	otizm = models.BooleanField(default=False, blank=False)
	TCStatus = models.IntegerField(default=0, blank=True)

	
	def clean(self):
		if not (self.bay or self.bayan or self.ucuncucins):
			raise ValidationError("Bay, bayan, veya ucuncu cins seciniz")
			
	class Meta:
		permissions = (
			("view_contact_info", "Can view contact info"),
		)
	

