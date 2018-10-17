from rest_framework import viewsets
from .models import Store, Coupon
from .serializers import StoreSerializer, CouponSerializer
from rest_framework.response import Response

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# Create your views here.

class CouponViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, TokenHasScope]
	queryset = Coupon.objects.filter()
	serializer_class = CouponSerializer

	def list(self, request, *args, **kwargs):
		self.queryset = Coupon.objects.filter(store=kwargs['store_id'])
		queryset = self.filter_queryset(self.get_queryset())

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)


class StoreViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, TokenHasScope]
	queryset = Store.objects.all();
	serializer_class = StoreSerializer