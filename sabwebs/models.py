from django.db import models
from django.contrib.auth.models import User

companies = (
		('Samsung','Samsung'),
		('Apple','Apple'),
		('Google','Google'),
		('Micromax','Micromax'),
		('Nokia','Nokia'),
	)
class product(models.Model):
	pid = models.AutoField(primary_key=True)
	p_name = models.CharField(max_length=100)
	p_desc = models.TextField()
	p_price = models.IntegerField()
	p_feature1 = models.CharField(max_length=100)
	p_feature2 = models.CharField(max_length=100)
        company = models.CharField(max_length=100,choices=companies)

	def __unicode__(self):
		return self.p_name

class prod_user(models.Model):
        uid = models.ForeignKey(User,blank=False, null=False)
        pid = models.ForeignKey(product,blank=False, null=False)
        nclick = models.IntegerField()
