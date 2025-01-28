from django.urls import path, re_path
from . import views
from rest_framework import routers
from .views import paymentviewset
from django.urls import path,include
router=routers.DefaultRouter()
router.register(r"payment",paymentviewset)


urlpatterns = [

    path('',include(router.urls)),
    path('verify_payment', views.verify_payment,name="   پرداخت  "),
    path('create_payment', views.create_payment,name="    ثبت و ذخیره    "),
   ]