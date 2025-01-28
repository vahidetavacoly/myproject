from django.shortcuts import render,redirect
from .forms import login_f,singup_f,LicenseForm,tamas_f,usertype_f,padcast_f,test_f,about_f,question_f,answer_f,image_f,vidio_f,blog_f,typem_f,typev_f,information_m_f
from .models import tamas,padcast,Profile,test,about,question,answer,image,vidio,blog,typem,typev,information_m
from rezerv.forms import AppointmentForm
from rezerv.models import Appointment 
from django.contrib.auth.models import User
from django.contrib.auth.decorators  import login_required
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from datetime import datetime,timedelta,date,time
from django.contrib.auth import authenticate,login,logout
from .userauth import userauth
from django.shortcuts import get_object_or_404,render
from django.core import serializers
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_GET

from rezerv.views import reservation_view,nobatk
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt


from django.db.models import Q
from django.core.cache import cache  # برای ذخیره کد لایسنس موقت
from django.utils import timezone
from twilio.rest import Client
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .utils import send_license_code_sms 

import datetime as dt
import socket
import re
from twilio.rest import Client
from django.core.cache import cache
from django.conf import settings
import random
import json
@login_required
@require_GET
@csrf_protect
@csrf_exempt
#import os
######################################################لاگین
def logins(request): 
    
    formsy = login_f(request.POST)
    return render(request, "Login.html", {"form": formsy})
     

def Register(request):
   form=singup_f()
   return render(request=request, template_name="Register.html",context={"form":form})
def sing_up(request):
    if request.method == "POST":
        formsy = singup_f(request.POST)  # فرض بر این است که singup_f فرم ثبت‌نام است
        if formsy.is_valid():
            # بررسی وجود نام کاربری
            userss = User.objects.filter(username=formsy.data["username"]).all()
            if len(userss) > 0:
                return HttpResponse("این نام کاربری قبلاً ثبت شده است.")

            # ایجاد کاربر جدید
            user = User.objects.create_user(
                username=formsy.data["username"],
                password=formsy.data["password"],
                email=formsy.data["username"]
            )
            user.firstname = formsy.data["namefull"]
            user.tell = formsy.data["tell"]  # اگر شماره تلفن در فرم ثبت است
            user.save()

            # ورود خودکار بعد از ثبت‌نام
            login(request, user)

            # هدایت به صفحه انتخاب نوع کاربر
            return redirect("/select_usertype")
        else:
            return HttpResponse("ثبت‌نام موفق نبود. لطفا دوباره امتحان کنید.")
    else:
        form = singup_f()
        return render(request, "Register.html", {"form": form})
       
def chekout(request):
    if request.user.is_authenticated:  # کاربر لاگین شده یا نه
        return HttpResponse("وارد شده")
    else:
        return HttpResponse("وارد نشده ")
def cheklogins(request):
    if request.method == "POST":
        formsy = login_f(request.POST)
        if formsy.is_valid():
            username = formsy.cleaned_data["username"]
            password = formsy.cleaned_data["password"]

            # احراز هویت
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # لاگین کاربر

                try:
                    # پیدا کردن نقش از Profile
                    profile = Profile.objects.get(user=user)
                    if profile.role == "client":  # بررسی نقش کاربر عادی
                        return redirect("/indexk")  # هدایت به صفحه کاربر عادی
                    elif profile.role == "moshaver":  # بررسی نقش مشاور
                        return redirect("/panel_moshaver")  # هدایت به پنل مشاور
                    else:
                        return HttpResponse("نقش کاربر تعیین نشده است. لطفاً با پشتیبانی تماس بگیرید.")
                except Profile.DoesNotExist:
                    return HttpResponse("برای این کاربر پروفایلی یافت نشد. لطفاً ثبت‌نام را تکمیل کنید.")
            else:
                return render(request, "Login.html", {"form": formsy, "error": "نام کاربری یا رمز عبور نادرست است."})
    else:
        formsy = login_f()
    return render(request, "Login.html", {"form": formsy})
def logouts(request):
    logout(request)
    return HttpResponseRedirect("/logins")


################################################
def index(request):
    List1=information_m.objects.all()
    List=tamas.objects.all()
    types=typem.objects.all()
    mm=information_m.objects.all()
    form=tamas_f()
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو 
   
     return render(request=request,template_name='Index.html',context={"user_st": user_st,"List1":List1,'types':types,'mm':mm,"List":List,"form":form})
def indexk(request):
    List1=information_m.objects.all()
    List=tamas.objects.all()
    types=typem.objects.all()
    mm=information_m.objects.all()
    form=tamas_f()
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو 

     return render(request=request,template_name='Indexk.html',context={"user_st": user_st,"List1":List1,'types':types,'mm':mm,"List":List,"form":form})
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
def list_filter(request,pk):#فیلتر بر اساس نوع مشاوره 
    type=get_object_or_404(typem,id=pk)
    
    filter=information_m.objects.filter(typetakhasos=type)
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]: 
      return render (request=request,template_name='filter1.html',context={'user_st':user_st,'filter':filter,'type':type}) 
def index2(request):
    search_query = request.GET.get('search', '')  # پارامتر جستجو از URL گرفته می‌شود
    moshaveran = []

    if search_query:
        # جستجو بر اساس نام مشاور
        moshaveran = information_m.objects.filter(namefull__icontains=search_query)

        if moshaveran.exists():
            # اگر بیش از یک مشاور پیدا شد، مشاور با نام جستجو شده را به ابتدای لیست بیاوریم
            moshaveran = sorted(moshaveran, key=lambda m: m.namefull.lower().startswith(search_query.lower()), reverse=True)
            
            # گرفتن شناسه‌های مشاوران پیدا شده
            highlighted_ids = ','.join(str(m.id) for m in moshaveran)

            # ریدایرکت به صفحه لیست مشاوران با شناسه‌های مشاوران پیدا شده
            return redirect(f"/path/to/list_moshaver1?highlighted_ids={highlighted_ids}")

    return render(request, 'indexk.html', {'moshaveran': moshaveran, 'search_query': search_query})
def filteres(request):#اچ تی ام ا لفیلتر
    
    return render(request=request,template_name='filter.html')
def filtered(request):
    name_query = request.GET.get('namefull', '')
    city_query = request.GET.get('city', '')

    # اگر نام یا شهر خالی نباشند، فیلتر کنیم
    filter_conditions = Q()
    if name_query:
        filter_conditions &= Q(namefull__icontains=name_query)  # برای جستجوی حساس به حروف کوچک و بزرگ
    if city_query:
        filter_conditions &= Q(city__icontains=city_query)  # جستجوی حساس به حروف کوچک و بزرگ در شهر

    # اعمال فیلترها
    doctor = information_m.objects.filter(filter_conditions)

    # اگر مشاورانی یافت نشد، پیام خطا نمایش می‌دهیم
    if not doctor.exists():
        return render(request, 'Reservationlist.html', {'message': 'مشاور مورد نظر در این شهر یافت نشد'})

    # در غیر این صورت، مشاوران فیلتر شده را به نمایش می‌گذاریم
    return render(request, 'filter.html', {
        'doctor': doctor,
        "name_query": name_query,
        "city_query": city_query,})
   

############################################# ثبت نام اولیه مشاور در سایت
def sabt_moshaver(request):
    formi=information_m_f()
    return render(request=request,template_name='sabt_moshaver.html',context={'form':formi})   

def create_moshaver(request):
    if request.method == 'POST':
        # بررسی اینکه آیا مشاور قبلاً ثبت نام کرده است
        if information_m.objects.filter(user=request.user).exists():
            return HttpResponse("شما قبلاً به عنوان مشاور ثبت شده‌اید. نمی‌توانید مجدد مشاور ثبت کنید.")
        
        # دریافت اطلاعات از فرم
        namefull = request.POST.get('namefull')  # نام کامل
        codemeli = request.POST.get('codemeli')  # کد ملی
        email = request.POST.get('email')  # ایمیل
        tell = request.POST.get('tell')  # شماره تلفن
        datetime = request.POST.get('datetime')  # تاریخ تولد
        jensiyat = request.POST.get('jensiyat')  # جنسیت
        mizantahsilat = request.POST.get('mizantahsilat')  # میزان تحصیلات
        typemadrak = request.POST.get('typemadrak')  # نوع مدرک
        savabeghtahsili = request.POST.get('savabeghtahsili')  # سوابق تحصیلی
        savabeghelmi = request.POST.get('savabeghelmi')  # سوابق علمی
        saltajrobe = request.POST.get('saltajrobe')  # سال‌های سابقه
        ostan = request.POST.get('ostan')  # استان
        city = request.POST.get('city')  # شهر
        adress = request.POST.get('adress')  # آدرس
        hazine = request.POST.get('hazine')  # هزینه مشاوره
        modat = request.POST.get('modat')  # مدت‌زمان مشاوره
        rozhozor = request.POST.get('rozhozor')  # روزهای حضور
        rozonline= request.POST.get('rozonline')  # روزهای حضور
        zaman = request.POST.get('zaman')  # زمان مشاوره
        biyografi = request.POST.get('biyografi')  # بیوگرافی
        start_time = request.POST.get('start_time')  # زمان شروع مشاوره
        end_time = request.POST.get('end_time')  # زمان پایان مشاوره
        imag = request.FILES.get('imag')  # عکس یا فایل آپلود شده
        typetakhasos_ids = request.POST.getlist('typetakhasos')  # تخصص‌های انتخاب شده (Many to Many)
        online_ids = request.POST.getlist('online')  # نوع ارتباط آنلاین (Many to Many)
       
        
        # ثبت اطلاعات مشاور جدید
        try:
            information = information_m.objects.create(
                user=request.user,  # ارتباط با کاربر جاری
                namefull=namefull,
                codemeli=codemeli,
                email=email,
                tell=tell,
                datetime=datetime,
                jensiyat=jensiyat,
                mizantahsilat=mizantahsilat,
                typemadrak=typemadrak,
                savabeghtahsili=savabeghtahsili,
                savabeghelmi=savabeghelmi,
                saltajrobe=saltajrobe,
                ostan=ostan,
                city=city,
                adress=adress,
                zaman=zaman,
                hazine=hazine,
                modat=modat,
                rozhozor=rozhozor,
                rozonline=rozonline,
                biyografi=biyografi,
                start_time=start_time,
                end_time=end_time,
                imag=imag,
            )

             # ذخیره ارتباط‌های Many-to-Many
            for typetakhasos_id in typetakhasos_ids:
                type_takhasos = typem.objects.get(id=typetakhasos_id)
                information.typetakhasos.add(type_takhasos)

            for online_id in online_ids:
                online_type = typev.objects.get(id=online_id)
                information.online.add(online_type)

            # هدایت به پنل مشاور
            return redirect("/panel_moshaver")

        except IntegrityError:
            return HttpResponse("خطا: کد ملی یا ایمیل تکراری است. لطفاً دوباره تلاش کنید.")
    else:
        return render(request, "sabt_moshaver.html")
def list_moshaver(request):
    tabel1=information_m.objects.all()
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی 
     return render(request=request,template_name="Reservationlist.html",context={"user_st": user_st,"tabel1":tabel1})       
def list_moshaver1(request):
    highlighted_ids = request.GET.get('highlighted_ids', '').split(',')
    highlighted_ids = [int(id) for id in highlighted_ids if id.isdigit()]  # تبدیل به لیست اعداد

    # مشاوران جستجو شده
    highlighted_moshaveran = information_m.objects.filter(id__in=highlighted_ids)

    # سایر مشاوران که در جستجو نبوده‌اند
    other_moshaveran = information_m.objects.exclude(id__in=highlighted_ids)

    user_st = userauth().state_and_login(request)
    print(user_st)

    if user_st["state"]:
        # ترکیب دو لیست: ابتدا مشاوران جستجو شده و سپس سایرین
        tabel1 = list(highlighted_moshaveran) + list(other_moshaveran)
        return render(request=request, template_name="Reservationlist.html", context={"user_st": user_st, "tabel1": tabel1})
# حذف مشاور
def delet_moshaver(request, pk):
    tabel = get_object_or_404(information_m, id=pk)
    if request.method == 'POST':
        tabel.delete()
        return HttpResponseRedirect('/list_moshaver')
    return render(request, 'delet_moshaver.html', {"tabel": tabel})

# به‌روزرسانی مشاور




def update_moshaver(request, information_id):
    information = get_object_or_404(information_m, id=information_id)
    if request.method == 'POST':
        form = information_m_f(request.POST, request.FILES)
        if form.is_valid():
            information.namefull = form.cleaned_data['namefull']
            information.codemeli = form.cleaned_data['codemeli']
            information.datetime = form.cleaned_data['datetime']
            information.jensiyat = form.cleaned_data['jensiyat']
            information.mizantahsilat = form.cleaned_data['mizantahsilat']
            information.typemadrak = form.cleaned_data['typemadrak']
            information.typetakhasos.set(form.cleaned_data['typetakhasos'])
            information.savabeghtahsili = form.cleaned_data['savabeghtahsili']
            information.savabeghelmi = form.cleaned_data['savabeghelmi']
            information.saltajrobe = form.cleaned_data['saltajrobe']
            information.ostan = form.cleaned_data['ostan']
            information.city = form.cleaned_data['city']
            information.adress = form.cleaned_data['adress']
            information.tell = form.cleaned_data['tell']
            information.imag = form.cleaned_data['imag']
            information.zaman = form.cleaned_data['zaman']
            information.online.set(form.cleaned_data['online'])
            information.modat = form.cleaned_data['modat']
            information.hazine = form.cleaned_data['hazine']
            information.rozhozor = form.cleaned_data['rozhozor']
            information.rozonline = form.cleaned_data['rozonline']
            information.email = form.cleaned_data['email']
            information.biyografi = form.cleaned_data['biyografi']
            information.start_time = form.cleaned_data['start_time']
            information.end_time = form.cleaned_data['end_time']
            information.save()
            return redirect("/panel_moshaver")
    else:
        initial_data = {
            'namefull': information.namefull,
            'codemeli': information.codemeli,
            'datetime': information.datetime,
            'jensiyat': information.jensiyat,
            'mizantahsilat': information.mizantahsilat,
            'typemadrak': information.typemadrak,
            'typetakhasos': information.typetakhasos.all(),
            'savabeghtahsili': information.savabeghtahsili,
            'savabeghelmi': information.savabeghelmi,
            'saltajrobe': information.saltajrobe,
            'ostan': information.ostan,
            'city': information.city,
            'adress': information.adress,
            'tell': information.tell,
            'imag': information.imag,
            'zaman': information.zaman,
            'online': information.online.all(),
            'modat': information.modat,
            'hazine': information.hazine,
            'rozhozor': information.rozhozor,
            'rozonline': information.rozonline,
            'email': information.email,
            'biyografi': information.biyografi,
            'start_time': information.start_time,
            'end_time': information.end_time,
            'id': information.id,
        }
        form = information_m_f(initial=initial_data)
    return render(request, 'update.html', {'form': form})
################################################پنل شخصی مشاور

def panel_moshaver(request):
    # بررسی لاگین بودن کاربر
    if request.user.is_authenticated:
        try:
            # گرفتن اطلاعات مشاور برای کاربر لاگین‌شده
            info = information_m.objects.get(user=request.user)

            # ارسال اطلاعات به قالب
            return render(
                request,
                "page_moshaverprivate.html",  # قالب مربوط به پنل مشاور
                {"info": info},  # ارسال اطلاعات مشاور
            )
        except information_m.DoesNotExist:
            return HttpResponse("هیچ اطلاعاتی برای شما یافت نشد. لطفاً ثبت مشاور را انجام دهید.")
    else:
        return redirect("/logins")
#######################################################پنل عمومی مشاور 
def page_moshaver1(request):
    tabelp=padcast.objects.all()
    tabelv=vidio.objects.all()
    tabelt=test.objects.all()
    tabela=image.objects.all()
    return render(request=request,template_name="page_moshaver.html", context={"tabelp":tabelp,"tabelv":tabelv,"tabelt":tabelt,"tabela":tabela, })   

def get(request, pk):
    # دریافت اطلاعات مشاور
    moshaver = get_object_or_404(information_m, id=pk)

    # دریافت لیست پادکست‌های مرتبط با مشاور از طریق فیلد user
    podcasts = padcast.objects.filter(user=moshaver.user)
    datav = vidio.objects.filter(user=moshaver.user)
    datat = test.objects.filter(user=moshaver.user)
    return render(request, "page_moshaver.html", {"consultant": moshaver, "podcasts": podcasts,"datav":datav,"datat":datat,})  
def consultant_podcasts(request, pk):
    # دریافت مشاور براساس ID
    consultant = get_object_or_404(information_m, id=pk)

    # دریافت لیست پادکست‌های مشاور
    podcasts = padcast.objects.filter(user=consultant.user)
   
    return render(request, "list.html", {"consultant": consultant, "podcasts": podcasts})      

def getv(request,pk):
    moshaver = get_object_or_404(information_m, id=pk)

    # دریافت لیست پادکست‌های مشاور
    datav = vidio.objects.filter(user=moshaver.user)

    return render(request, "list.html", {"consultant": moshaver, "datav": datav})      
      
def gett(request,pk):
    moshaver = get_object_or_404(information_m, id=pk)

    # دریافت لیست پادکست‌های مشاور
    datat = test.objects.filter(user=moshaver.user)

    return render(request, "list.html", {"consultant": moshaver, "datat": datat})      
        

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
# حذف درباره ما
def delet_about(request, id):
    tabel = get_object_or_404(about, id=id)
    if request.method == 'POST':
        tabel.delete()
        return HttpResponseRedirect('/list_about')
    return render(request, 'delet_about.html', {"tabel": tabel})

# به‌روزرسانی درباره ما
def update_about(request, id):
    tabel = get_object_or_404(about, id=id)
    if request.method == 'POST':
        form = about_f(request.POST, instance=tabel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_about')
    else:
        form = about_f(instance=tabel)
    return render(request, 'sabt_about.html', {'form': form})
##################################################################وبلاگ
def Blog(request):
    tabel=blog.objects.all()
    form=blog_f()
    # اگر وضعیت رو کخ ریگشنری هست رو 
    return render(request=request, template_name="sabt_blog.html",context={'form':form,"tabel":tabel,})
def Blogdetails(request):
   
    return render(request=request, template_name="Blogdetails.html")
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
# حذف وبلاگ
def delet_blog(request, id):
    tabel = get_object_or_404(blog, id=id)
    if request.method == 'POST':
        tabel.delete()
        return HttpResponseRedirect('/list_blog')
    return render(request, 'delet_blog.html', {"tabel": tabel})

# به‌روزرسانی وبلاگ
def update_blog(request, id):
    tabel = get_object_or_404(blog, id=id)
    if request.method == 'POST':
        form = blog_f(request.POST, instance=tabel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list_blog')
    else:
        form = blog_f(instance=tabel)
    return render(request, 'sabt_blog.html', {'form': form})
##################################################################
def Faq(request):      
    tabel = question.objects.all()
    form=question_f()
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی
        tabel1= question.objects.filter(user_id=user_st["user"].id)
    
    return render(request=request, template_name="Faq.html",context={"user_st": user_st,'form':form,"tabel": tabel,"tabel1":tabel1}) 
def list_Faq(request):
    tabel = question.objects.all()
    forms = answer_f()
    return render(request=request, template_name="sabt_Faq.html",
                  context={"tabel": tabel,'forms':forms})
def get_ask_with_comment(request,pk):

    print(pk)
    askis= get_object_or_404(answer.objects.select_related('soal'), id=pk)
    print(askis.caption)

    return render(request=request, template_name="answer.html", context={"listmyjavab": askis})
def delete_Faq(request):
    if request.method == "POST":
        id = request.POST.get("id")
        question.objects.filter(id=id).delete()
        return HttpResponse("/true")
    else:
        return HttpResponse("false")
def create_Faq(request):
       if request.method=="POST":
             forms=question_f(request.POST)

             if forms.is_valid():
                user_st= userauth().state_and_login(request)
                id=forms.data["id"]
                if id=="0":
                   datast=question.objects.filter(title=forms.data["title"]).all()
                   if len(datast)>0:
                    return HttpResponse("exit")
               
                   newask=question(title=forms.data["title"],caption=forms.data["caption"],
                              user_id= user_st["user"].id
                               )

                   newask.save()
                   return HttpResponse("true")
                else:
                    editask=question.objects.filter(id=id).first()
                    editask.title=forms.data["title"]
                    editask.caption=forms.data["caption"]
                  
                    editask.save()
                    return HttpResponse("true")
             else:    
              return HttpResponse("valid")
       else:
              return HttpResponse("false")
def answer_d(request):
    tabel = question.objects.all()
    form=answer_f()
    return render(request=request, template_name="sabt_Faq.html",context={'form':form,"tabel":tabel})    
def update_answer(request,id):
    tabel=get_object_or_404(answer,id=id)
    if request.method=='POSt':
        form=answer_f(request.POSt,instance=tabel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('answer')
    else:
      form=answer_f(instance=tabel)
    return render(request,template_name='sabt_answer.html',context={'form':form})          
def delet_answer(request,id):
    tabel=get_object_or_404(answer,id=id) 
    if request.method=='POSt':
        tabel.adelete()
        return HttpResponseRedirect('answer')
    return render(request=request,template_name='delet_answer',context={"tabel":tabel})
def create_answer(request):
    if request.method == "POST":
        formj = answer_f(request.POST)
        print(formj.data)
        if formj.is_valid():
            user_st = userauth().state_and_login(request)

           
            newask = answer(caption=formj.data["caption"],soal_id=formj.data["soal_id"],user_id=user_st["user"].id)
            newask.save()
            return HttpResponse("true")
        else:    
         return HttpResponse("valid")
    else:
        return HttpResponse("false")
#################################################################نظرات
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
# حذف نظر
def delet_ContactUs(request, id):
    result = get_object_or_404(tamas, id=id)
    if request.method == 'POST':
        result.delete()
        return HttpResponseRedirect('/mycomment')
    return render(request, 'delet_contact.html', {"result": result})

# به‌روزرسانی نظر
def update_ContactUs(request, id):
    result = get_object_or_404(tamas, id=id)
    if request.method == 'POST':
        form = tamas_f(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mycomment')
    else:
        form = tamas_f(instance=result)
    return render(request, 'ContactUs.html', {'form': form})
##########################################################################گالری
def gallery_2(request):
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی
        tabel= image.objects.filter(user_id=user_st["user"].id).all()
        form=image_f()
        return render(request=request, template_name="upload_image.html",
               context={"user_st": user_st,"tabel":tabel,'form':form})
    else:
          return HttpResponse("وارد نشده 403 ")      
def list_img(request):
    tabel=image.objects.all()
    return render(request=request,template_name="filter.html",context={"tabel":tabel})       

def create_img(request):    
     if request.method=="POST":
            forms=image_f(request.POST,request.FILES)
            print(forms.data)
            if forms.is_valid():
                user_st= userauth().state_and_login(request)
                id=forms.data["id"]
                if id=="0":
                   datast=image.objects.filter(title=forms.data["title"]).all()
                   if len(datast)>0:
                    return HttpResponse("exit")
                   x=datetime.datetime.now()
                   newask=image(   title =forms.data["title"] ,     
                                        img = request.FILES["img"],     
                                   
                                       user_id= user_st["user"].id ) 
                           
   
   
                   newask.save()
                   return HttpResponse("true")
                else:
                    editask=image.objects.filter(id=id).first()
                    editask.title =forms.data["title"] ,       
                    editask.img = request.FILES["img"],     
                  
                    editask.save()
                    return HttpResponse("true")
            else:
              return HttpResponse("valid")
     else:
              return HttpResponse("false")             

# حذف تصویر
def delet_img(request, id):
    tabel = get_object_or_404(image, id=id)
    if request.method == 'POST':
        tabel.delete()
        return HttpResponseRedirect('/list_img')
    return render(request, 'delet_img.html', {"tabel": tabel})

# به‌روزرسانی تصویر
def update_image(request, id):
    image_instance = get_object_or_404(image, id=id)
    if request.method == 'POST':
        form = image_f(request.POST, request.FILES)
        if form.is_valid():
            image_instance.title = form.cleaned_data['title']
            if 'image' in request.FILES:
                image_instance.image = request.FILES['image']
            image_instance.save()
            return redirect('panel_moshaver')
    else:
        initial_data = {
            'title': image_instance.title,
            'image': image_instance.image,
            'id': image_instance.id,
        }
        form = image_f(initial=initial_data)
    return render(request, 'upload_image.html', {'form': form})
#####################################################################پادکست ها 
def padcast_d(request):
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی
        tabel= padcast.objects.filter(user_id=user_st["user"].id).all()
        form=padcast_f()
        return render(request=request, template_name="sabt_padcast.html",
               context={"user_st": user_st,"tabel":tabel,'form':form})
    else:
          return HttpResponse("وارد نشده 403 ")
    #tabel=padcast.objects.all()
    #form=padcast_f()
    #return render(request=request, template_name="sabt_padcast.html",context={'form':form,"tabel":tabel})
def list_padcast(request):
    tabelp=padcast.objects.all()
    return render(request=request,template_name="padcast.html",context={"tabelp":tabelp})       

def create_padcast(request):    
     if request.method=="POST":
            #file=request.FILES.get('file'),
            forms=padcast_f(request.POST,request.FILES)
            print(forms.data)
            if forms.is_valid():
                user_st= userauth().state_and_login(request)
                id=forms.data["id"]
                if id=="0":
                   datast=padcast.objects.filter(title=forms.data["title"]).all()
                   if len(datast)>0:
                    return HttpResponse("exit")
              
                   newask=padcast(title=forms.data["title"],   
                                        caption=forms.data["caption"],     
                                        audio=request.FILES["audio"],     
                                        #file=file,
                                        user_id=user_st["user"].id 
                                        ) 
                               

                   newask.save()
                   return HttpResponse("true")
                else:
                    editask=padcast.objects.filter(id=id).first()
                    editask.title =forms.data["title"] ,   
                    editask.caption = forms.data["caption"] ,     
                    #editask.audio = request.FILES["audio"],     
                    #editask.file=request.FILES.get('file'), 
                  
                    editask.save()
                    return HttpResponse("true")
            else:
              return HttpResponse("valid")
     else:
              return HttpResponse("false")             
# حذف پادکست
def delet_padcast(request, id):
    tabel = get_object_or_404(padcast, id=id)
    if request.method == 'POST':
        tabel.delete()
        return HttpResponseRedirect('/list_padcast')
    return render(request, 'delet_padcast.html', {"tabel": tabel})

# به‌روزرسانی پادکست
def update_padcast(request, id):
    podcast_instance = get_object_or_404(padcast, id=id)
    if request.method == 'POST':
        form = padcast_f(request.POST, request.FILES)
        if form.is_valid():
            podcast_instance.title = form.cleaned_data['title']
            podcast_instance.caption = form.cleaned_data['caption']
            if 'audio' in request.FILES:
                podcast_instance.audio = request.FILES['audio']
            podcast_instance.save()
            return redirect('panel_moshaver')
    else:
        initial_data = {
            'title': podcast_instance.title,
            'caption': podcast_instance.caption,
            'audio': podcast_instance.audio,
            'id': podcast_instance.id,
        }
        form = padcast_f(initial=initial_data)
    return render(request, 'update_padcast.html', {'form': form})
###################################################################تست ها 
def test_d(request):
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی
        tabel= test.objects.filter(user_id=user_st["user"].id).all()
        form=test_f()
        return render(request=request, template_name="sabt_test.html",
               context={"user_st": user_st,"tabel":tabel,'form':form})
    else:
          return HttpResponse("وارد نشده 403 ")    
def create_test(request):
    if request.method == 'POST':
        form = test_f(request.POST)
        if form.is_valid():
            test_instance = test(
                name=form.cleaned_data['name'],
                soal=form.cleaned_data['soal'],
                result=form.cleaned_data['result']
            )
            test_instance.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})
def delete_test(request, id):
    test_instance = get_object_or_404(test, id=id)
    if request.method == 'POST':
        test_instance.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
def update_test(request, id):
    test_instance = get_object_or_404(test, id=id)
    if request.method == 'POST':
        form = test_f(request.POST)
        if form.is_valid():
            test_instance.name = form.cleaned_data['name']
            test_instance.soal = form.cleaned_data['soal']
            test_instance.result = form.cleaned_data['result']
            test_instance.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False})
def list_test(request):
    user_st = userauth().state_and_login(request)
    if user_st["state"]:
        tabel = test.objects.filter(user_id=user_st["user"].id).all()
        return render(request, 'list_test.html', {'user_st': user_st, 'tabel': tabel})
    else:
        return HttpResponse("وارد نشده 403")
############################################### ویدیو
def vidio_d(request):
    user_st = userauth().state_and_login(request)
    print(user_st)
    if user_st["state"]:  # اگر وضعیت رو کخ ریگشنری هست رو گرفتی
        tabel= vidio.objects.filter(user_id=user_st["user"].id).all()
        form=vidio_f()
        return render(request=request, template_name="sabt_vidio.html",
               context={"user_st": user_st,"tabel":tabel,'form':form})
    else:
          return HttpResponse("وارد نشده 403 ")   
def create_vidio(request):    
     if request.method=="POST":
            forms=vidio_f(request.POST,request.FILES)
            print(forms.data)
            if forms.is_valid():
                user_st= userauth().state_and_login(request)
                id=forms.data["id"]
                if id=="0":
                   datast=vidio.objects.filter(title=forms.data["title"]).all()
                   if len(datast)>0:
                    return HttpResponse("exit")
                   x=datetime.datetime.now()
                   newask=vidio(   title =forms.data["title"] ,     
                                        video = request.FILES["video"],     
                                
                                       user_id= user_st["user"].id ) 
                          
   
                   newask.save()
                   return HttpResponse("true")
                else:
                    editask=vidio.objects.filter(id=id).first()
                    editask.title =forms.data["title"] ,       
                    editask.video = request.FILES["video"],     
                
                  
                    editask.save()
                    return HttpResponse("true")
            else:
              return HttpResponse("valid")
     else:
              return HttpResponse("false")             
    
def list_vidio(request):
    tabel=vidio.objects.all()
    return render(request=request,template_name="vidio.html",context={"tabel":tabel})       
# حذف ویدیو
def delet_vidio(request, id):
    tabel = get_object_or_404(vidio, id=id)
    if request.method == 'POST':
        tabel.delete()
        return HttpResponseRedirect('/list_vidio')
    return render(request, 'delet_vidio.html', {"tabel": tabel})

# به‌روزرسانی ویدیو
def update_vidio(request, id):
    vidio_instance = get_object_or_404(vidio, id=id)
    if request.method == 'POST':
        form = vidio_f(request.POST, request.FILES)
        if form.is_valid():
            vidio_instance.title = form.cleaned_data['title']
            if 'video' in request.FILES:
                vidio_instance.video = request.FILES['video']
            vidio_instance.save()
            return redirect('panel_moshaver')
    else:
        initial_data = {
            'title': vidio_instance.title,
            'video': vidio_instance.video,
            'id': vidio_instance.id,
        }
        form = vidio_f(initial=initial_data)
    return render(request, 'sabt_vidio.html', {'form': form})
########################################################


   

def select_usertype(request):
    if request.method == "POST":
        form = usertype_f(request.POST)
        if form.is_valid():
            user_type = form.cleaned_data["user_type"]  # نوع کاربر

            # ذخیره نقش کاربر در مدل Profile
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.role = user_type
            profile.save()

            # هدایت بر اساس نقش
            if user_type == "client":
                return redirect("/indexk")  # کاربر عادی به ایندکس عادی
            elif user_type == "moshaver":
                return redirect("/send_docs")  # مشاور به صفحه ارسال مدارک
    else:
        form = usertype_f()
    return render(request, "user_type.html", {"form": form})



##################################

def is_valid_phone_number(phone_number):
    pattern = r'^\+?1?\d{9,15}$'  # الگوی شماره موبایل بین‌المللی
    return re.match(pattern, phone_number) is not None         
def validate_license_code(code):
    # لیست کدهای معتبر
    valid_codes = ['VALID_CODE1', 'VALID_CODE2', 'VALID_CODE3']  # به‌روزرسانی این کدها
    return code in valid_codes
def send_docs(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("document")
        # انجام اعتبارسنجی فایل (مثال: بررسی فرمت یا اندازه فایل)
        # اگر مورد قبول بود، به مرحله بعد هدایت کنید
        license_code = random.randint(100000, 999999)
        cache.set("license_code", str(license_code), timeout=300)  # کد لایسنس برای 5 دقیقه معتبر است
        # شبیه‌سازی ارسال پیامک یا ایمیل
        print(f"License Code Generated and Sent: {license_code}")
        return redirect("/verify_license")
    return render(request, "send_docs.html")

def verify_license(request):
    if request.method == "POST":
        entered_code = request.POST.get("license_code")
        saved_code = cache.get("license_code")
        if saved_code:
            if entered_code == saved_code:
                return redirect("/sabt_moshaver")
            else:
                return render(request, "license_verification.html", {"error": "Invalid License Code"})
        else:
            return render(request, "license_verification.html", {"error": "No License Code found in cache."})
    else:
        license_code = random.randint(100000, 999999)
        cache.set("license_code", str(license_code), timeout=300)  # کد لایسنس برای 5 دقیقه معتبر است
        print(f"License Code Generated and Sent: {license_code}")  # شبیه‌سازی ارسال پیامک یا ایمیل
        return render(request, "license_verification.html")

###########################
def send_license_code_to_mobile(phone_number, license_code):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Your License Code is: {license_code}",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    print(f"Message sent to {phone_number} with SID: {message.sid}")

def send_docs1(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("document")
        # انجام اعتبارسنجی فایل (مثال: بررسی فرمت یا اندازه فایل)
        # اگر مورد قبول بود، به مرحله بعد هدایت کنید
        license_code = random.randint(100000, 999999)
        cache.set("license_code", str(license_code), timeout=300)  # کد لایسنس برای 5 دقیقه معتبر است
        phone_number = request.POST.get("phone_number")
        send_license_code_to_mobile(phone_number, license_code)
        return redirect("/verify_license")
    return render(request, "send_docs.html")
def verify_license1(request):
    if request.method == "POST":
        entered_code = request.POST.get("license_code")
        saved_code = cache.get("license_code")
        if saved_code:
            if entered_code == saved_code:
                return redirect("/sabt_moshaver")
            else:
                return render(request, "license_verification.html", {"error": "Invalid License Code"})
        else:
            return render(request, "license_verification.html", {"error": "No License Code found in cache."})
    else:
        license_code = random.randint(100000, 999999)
        cache.set("license_code", str(license_code), timeout=300)  # کد لایسنس برای 5 دقیقه معتبر است
        print(f"License Code Generated and Sent: {license_code}")  # شبیه‌سازی ارسال پیامک یا ایمیل
        return render(request, "license_verification.html")