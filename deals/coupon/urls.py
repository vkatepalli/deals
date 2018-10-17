from django.urls import path, include
from . import views
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
router.register('store', views.StoreViewSet)
router.register(r'store/(?P<store_id>\d+)/coupon', views.CouponViewSet)
urlpatterns = router.urls
