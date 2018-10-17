from django.contrib import admin

# Register your models here.
from .models import Store, Coupon
admin.site.register(Store)
admin.site.register(Coupon)
