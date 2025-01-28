from django.shortcuts import render
from django.shortcuts import render,redirect
from app.forms import login_f,singup_f,tamas_f,AppointmentForm,usertype_f,padcast_f,test_f,about_f,question_f,answer_f,image_f,vidio_f,blog_f,typem_f,typev_f,information_m_f
from .models import tamas,padcast,test,about,question,answer,image,vidio,blog,typem,typev,information_m,Appintment
from django.contrib.auth.models import User
from django.contrib.auth.decorators  import login_required
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
#from .userauth import userauth
from django.shortcuts import get_object_or_404,render
from django.core import serializers
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_GET
from datetime import datetime,timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import datetime as dt
import socket
import datetime
from django.utils import timezone
from datetime import datetime,date,time
@login_required
@require_GET
@csrf_protect
@csrf_exempt
#import os
# Create your views here.
def takhasos(request):
    formsy=typem_f()
    return render(request=request,template_name='type.html',context={'formsy':formsy})
def nomoshavere(request):
    forms=typev_f()
    return render(request=request,template_name='typev.html',context={'forms':forms})
def savetakhasos(request):    
        if request.method == "POST":
                    formsy = typem_f(request.POST)
                    print(formsy.data)
                    us = typem(
                        name=formsy.data["name"]
                        
                        )
                    us.save()
                    return HttpResponseRedirect("/takhasos")            
        else:
                return HttpResponse("خطا")            
def savenomoshavere(request):
        if request.method == "POST":
                    forms= typev_f(request.POST)
                    print(forms.data)
                    us = typev(
                        name=forms.data["name"],
                        
                        )
                    us.save()
                    return HttpResponseRedirect("/nomoshavere")            
        else:
                return HttpResponse("خطا")
################################################################درباره ی ما
def AboutUs(request):
    form=about_f()
    return render(request=request, template_name="sabt_about.html",context={'form':form})
def create_about(request):
    if request.method=='POST':
            form=about_f(request.POST)
            if form.is_valid():
        
                us=about(caption=form.data["caption"])
                us.save()
                return HttpResponse("ثبت شد ")
    else:
            return HttpResponse("ثبت نشد ")
def list_about(request):
    about1=about.objects.all()
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفت
      return render(request=request,template_name="AboutUs.html",context={"about1":about1,"user_st": user_st})       
def update_about(request,id):
    tabel=get_object_or_404(about,id=id)
    if request.method=='POSt':
        form=about_f(request.POSt,instance=tabel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('about')
    else:
      form=about_f(instance=tabel)
    return render(request,template_name='sabt_about.html',context={'form':form})          
def delet_about(request,id):
    tabel=get_object_or_404(about,id=id) 
    if request.method=='POSt':
        tabel.adelete()
        return HttpResponseRedirect('about')
    return render(request=request,template_name='delet_about',context={"tabel":tabel})
##################################################################وبلاگ
def Blog(request):
    tabel=blog.objects.all()
    form=blog_f()
    # اگر وضعیت رو کخ ریگشنری هست رو 
    return render(request=request, template_name="sabt_blog.html",context={'form':form,"tabel":tabel,})
def Blogdetails(request):
   
    return render(request=request, template_name="Blogdetails.html")
def create_blog1(request):
    if request.method=='POSt':
        form=blog_f(request.POSt,request.FILES)
        if form.is_valid():
            #user_st = userauth().state_and_login(request)
            #us= blog( user_id=user_st["user"].id )
            us=blog(   title =form.data["title"] ,
                        caption =form.data["caption"] , 
                        file =form.data["file"]  ,
                        tarikhenteshar =form.data["tarikhenteshar"] ,)
            us.save()
            return HttpResponseRedirect("ثبت شد")
        else:
             return HttpResponseRedirect("ثبت نشد")
            #form=blog_f()
        #return render(request,template_name='sabt_blog.html',context={'form':form})  
def create_blog(request):    
     if request.method=="POST":
             forms=blog_f(request.POST)

             if forms.is_valid():
                #user_st= userauth().state_and_login(request)
                id=forms.data["id"]
                if id=="0":
                   datast=blog.objects.filter(title=forms.data["title"]).all()
                   if len(datast)>0:
                    return HttpResponse("exit")
                   x=datetime.datetime.now()
                   newask=blog( title =forms.data["title"] ,
                        caption =forms.data["caption"] , 
                       
                        tarikhenteshar =x)
                            #user_id= user_st["user"].id 

 
 
   
  
                   newask.save()
                   return HttpResponse("true")
                else:
                    editask=blog.objects.filter(id=id).first()
                    editask.title =forms.data["title"] ,
                    editask.caption=forms.data["caption"]
                 
                    editask.tarikhenteshar =x
                    editask.save()
                    return HttpResponse("true")
             else:
              return HttpResponse("valid")
     else:
              return HttpResponse("false")             
def list_blog(request):
    tabel=blog.objects.all()
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو 
     return render(request=request,template_name="Blog.html",context={"tabel":tabel,"user_st": user_st,})   
def delet_blog(request):
    if request.method == "POST":
        id = request.POST.get("id")
        vidio.objects.filter(id=id).delete()
        return HttpResponse("/true")
    else:
        return HttpResponse("false")        
def update_blog(request,id):
    tabel=get_object_or_404(blog,id=id)
    if request.method=='POSt':
        form=blog_f(request.POSt,instance=tabel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/Blog')
    else:
      form=blog_f(instance=tabel)
    return render(request,template_name='sabt_blog.html',context={'form':form})          
def delet_blog1(request,id):
    tabel=get_object_or_404(blog,id=id) 
    if request.method=='POSt':
        tabel.adelete()
        return HttpResponseRedirect('Blog')
    return render(request=request,template_name='delet_blog',context={"tabel":tabel})
##################################################################                
def ContactUs(request):
    form=tamas_f()
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفت
      return render(request=request,template_name="ContactUs.html",context={'form':form,"user_st": user_st})
def contact(request): 
    action = "/contact"
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    print(ip_adress)
    if request.method == "POST":
        form = tamas_f(request.POST)
        print(form.data)
        if form.is_valid():
          result =tamas(name=form.data["name"], email=form.data["email"], ip=ip_adress,payam=form.data["payam"])
          result.save()
          return HttpResponseRedirect("/mycomment") 
        else:
          return render(request=request, template_name="ContactUs.html", context={"form": form})

    form = tamas_f()
    return render(request=request, template_name="ContactUs.html", context={"form": form, "action": action})
def mycomment(request):  # بعد از زدن ارسال این تابع اجرا میشه
    hostname = socket.gethostname()
    ip_adress = socket.gethostbyname(hostname)
    List = tamas.objects.filter(ip=ip_adress).all()
    form= tamas_f()
    return render(request=request, template_name="Index.html", context={"List": List, "form": form})
def update_ContactUs(request, id):  # برای ویرایش
    result = tamas.objects.filter(id=id).first()
    action = "/editsave"
    form = tamas_f(initial={"id": id, "name": result.name, "email": result.email, "payam": result.payam})
    return render(request=request, template_name="ContactUs.html", context={"form ": form, "action": action})
def update_ContactUs(request):  # برای ویرایش
    if request.method == "POST":
        forms = tamas_f(request.POST)
        id = forms.data["id"]
        result = tamas.objects.filter(id=id).first()
        result.name = forms.data["name"]
        result.email = forms.data["email"]
        result.payam = forms.data["payam"]
        result.save()
        return HttpResponseRedirect("/mycomment")
def delet_ContactUs(request, id):  # برای حذف
    result = tamas.objects.filter(id=id).first()
    result.delete()
    return HttpResponseRedirect("/mycomment")