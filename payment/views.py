from django.shortcuts import render
from .models import payment
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.conf import settings
import json
#import requests
from rest_framework import viewsets
from .models import payment
from .serializer import serializerpayment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
class paymentviewset(viewsets.ModelViewSet):
    queryset =payment.objects.all()
    serializer_class =serializerpayment

def create_payment(request):
    mablagh=1000
    shenase_kharid='ORD123456'
    payload={
        'merchant_id':settings.ZARINPAL_MERCHANT_ID,
        'mablagh':mablagh,
        'callback_url':'https://loacalhost:8000/payment/verify',#بازگشتی بعد از پرداخت url
        'descrition':'پرداخت برای رزرو شماره'+ shenase_kharid,
    }
    response=request.post(settings.ZARINPAL_URL,data=payload)
    result=response.json()
    if result['status'] ==100:
        authority=result['authority']
        payment=payment.objects.create(shenase_kharid=shenase_kharid,mablagh=mablagh,authority=authority)
        return redirect(f'https:///www.zarinpal.com/pgw/payment/{authority}')
    else:
        return JsonResponse({'error':'خطا در ارتباط با زرین پال '})
def  verify_payment(request):
      authority=request.GET.get('Authority')
      status=request.GET.get('Status')
      if status=='OK':
        payload={
            'merchant_id':settings.ZARINPAL_MERCHANT_ID,
            'authority':authority,
            'mablagh':1000,
        }
        response=request.post(settings.ZARINPAL_VERINPAL_URL,data=payload)
        result=response.json()
        if result['status'] ==100: 
            payment=payment.objects.get(authority=authority)
            payment.status='paid'
            payment.save()
            return render(request,"payment_succss.html",{'payment':payment})
        else:
           return render(request,"payment_faild.html") 
      else:
          return render(request,"payment_faild.html")       