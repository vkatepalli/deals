import datetime
from django.db import models
from django.utils import timezone

class Store(models.Model):
    store_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.store_name

class Coupon(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    offer_type = models.CharField(max_length=50)
    offer_code = models.CharField(max_length=50)
    offer_value = models.IntegerField(default=0)

    def __str__(self):
    	return self.title

  #   def was_published_recently(self):
		# return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
