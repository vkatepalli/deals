from rest_framework import serializers
from .models import Store, Coupon

class StoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Store
		fields = ('id', 'store_name', 'category', 'pub_date')

class CouponSerializer(serializers.ModelSerializer):
	class Meta:
		model = Coupon
		fields = ('id', 'title', 'description', 'offer_type', 'offer_code', 'offer_value', 'store')