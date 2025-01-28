from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
import calendar
from app.userauth import userauth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from app.forms import login_f,singup_f,LicenseForm,tamas_f,usertype_f,padcast_f,test_f,about_f,question_f,answer_f,image_f,vidio_f,blog_f,typem_f,typev_f,information_m_f
from app.models import tamas,padcast,Profile,test,about,question,answer,image,vidio,blog,typem,typev,information_m
from .forms import AppointmentForm
from .models import Appointment,Message
from django.views.decorators.csrf import csrf_exempt

import json
import twilio
print(twilio.__version__)

@login_required



def submit_reservation(request, pk):
    consultant = get_object_or_404(information_m, id=pk)  # اطلاعات مشاور را پیدا می‌کنیم
    user = request.user  # دریافت کاربر جاری

    if request.method == "POST":
        # گرفتن اطلاعات از فرم
        appointment_type = request.POST.get("appointment_type")
        date_str = request.POST.get("date")
        time_str = request.POST.get("time")

        if not date_str or not time_str or not appointment_type:
            # اگر اطلاعات ناقص بود، خطا را برگردان
            return JsonResponse({"success": False, "error": "تمام فیلدها باید پر شوند."})

        try:
            # تبدیل تاریخ و ساعت به فرمت مناسب
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            selected_time = datetime.strptime(time_str, "%H:%M").time()

            # ذخیره نوبت در دیتابیس
            new_appointment = Appointment.objects.create(
                user=user,
                consultant=consultant,
                date=selected_date,
                time=selected_time,
                appointment_type=appointment_type
            )

            # نتیجه ثبت موفق
            if appointment_type == "online":
                # هدایت به پنل آنلاین (می‌توانید لینک دلخواه برای جلسه آنلاین اضافه کنید)
                return redirect("online_panel", appointment_id=new_appointment.id)  # پنلی که جلسه آنلاین برگزار می‌شود
            else:
                # نمایش پیام "ثبت شد"
                return render(request, "success_message.html", {"message": "نوبت شما با موفقیت ثبت شد. در ساعت و تاریخ مشخص شده حضوری مراجعه کنید."})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "درخواست نامعتبر بود."}, status=400)

def appointment_success(request, pk):#تایید رزرو حضوری
    appointment = get_object_or_404(Appointment, id=pk)
    context = {
        "appointment": appointment,
        "consultant": appointment.consultant,
        "user": appointment.user,
    }
    return render(request, "appointment_success.html", context)

def reservation_view(request, pk):
    consultant = get_object_or_404(information_m, id=pk)  # دریافت اطلاعات مشاور
    user = request.user  # دریافت کاربر جاری

    if request.method == "POST":
        # گرفتن اطلاعات تاریخ، ساعت، و نوع نوبت از فرم
        appointment_type = request.POST.get("appointment_type")
        date_str = request.POST.get("date")
        time_str = request.POST.get("time")

        if not date_str or not time_str or not appointment_type:
            context = {"error": "اطلاعات ناقص است."}
            return render(request, "Reservation.html", context)

        try:
            # تبدیل تاریخ و ساعت به فرمت مناسب
            selected_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            selected_time = datetime.strptime(time_str, "%H:%M").time()

            # بررسی می‌کنیم که آیا نوبتی برای این ساعت و تاریخ وجود دارد یا خیر
            existing_appointment = Appointment.objects.filter(
                consultant=consultant,
                date=selected_date,
                time=selected_time
            ).exists()

            if existing_appointment:
                # نوبت قبلاً رزرو شده است، ساعت را از لیست حذف می‌کنیم
                available_times = get_available_times(consultant, selected_date)
                context = {
                    "error": "این ساعت قبلاً رزرو شده است. لطفاً ساعت دیگری انتخاب کنید.",
                    "available_times": available_times
                }
                return render(request, "Reservation.html", context)

            # ثبت نوبت جدید
            new_appointment = Appointment.objects.create(
                user=user,
                consultant=consultant,
                date=selected_date,
                time=selected_time,
                appointment_type=appointment_type
            )

            # هدایت به صفحه مربوط به رزرو آنلاین یا حضوری
            if appointment_type == "online":
                return redirect("online_meeting", pk=new_appointment.id)
            else:
                return redirect("appointment_success", pk=new_appointment.id)

        except Exception as e:
            context = {"error": str(e)}
            return render(request, "Reservation.html", context)

    # نمایش تاریخ‌ها و ساعت‌های ممکن
    today = datetime.today()
    available_dates = [today + timedelta(days=i) for i in range(7)]
    available_times = []

    # تقسیم ساعت‌ها به بازه نیم‌ساعته
    start_time = datetime.combine(today, consultant.start_time)
    end_time = datetime.combine(today, consultant.end_time)
    while start_time.time() < end_time.time():
        available_times.append(start_time.time().strftime("%H:%M"))
        start_time += timedelta(minutes=30)

    # حذف ساعت‌های رزرو شده از لیست
    selected_date = request.GET.get("date")  # در صورت لزوم تاریخ انتخابی را از querystring دریافت می‌کنیم
    if selected_date:
        selected_date = datetime.strptime(selected_date, "%Y-%m-%d").date()
        available_times = get_available_times(consultant, selected_date)

    context = {
        "consultant": consultant,
        "user_id": user.id,
        "available_dates": available_dates,
        "available_times": available_times,
    }
    return render(request, "Reservation.html", context)
# تابع برای دریافت ساعت‌های آزاد برای یک تاریخ خاص
def get_available_times(consultant, selected_date):
    existing_appointments = Appointment.objects.filter(
        consultant=consultant,
        date=selected_date
    )

    # لیستی از ساعت‌هایی که قبلاً رزرو شده‌اند
    booked_times = [appointment.time.strftime("%H:%M") for appointment in existing_appointments]

    # تقسیم ساعت‌ها به بازه نیم‌ساعته
    available_times = []
    start_time = datetime.combine(selected_date, consultant.start_time)
    end_time = datetime.combine(selected_date, consultant.end_time)
    while start_time.time() < end_time.time():
        time_str = start_time.time().strftime("%H:%M")
        if time_str not in booked_times:
            available_times.append(time_str)
        start_time += timedelta(minutes=30)

    return available_times



def all_appointments(request):#لسیت کل نوبت ها
    # دریافت لیست کامل نوبت‌ها
    appointments = Appointment.objects.all().order_by('-date', '-time')  # مرتب‌سازی بر اساس تاریخ و زمان (به صورت نزولی)

    # ارسال داده‌ها به قالب HTML
    return render(request, 'all_apppoint.html', {'appointments': appointments})

###################################################################

def start_session(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)

    # فقط مشاور می‌تواند جلسه را شروع کند
    if appointment.consultant.user == request.user:
        appointment.status = 'in_progress'
        appointment.save()

        return redirect('online_meeting', pk=appointment.id)  # هدایت به پنل آنلاین

    return redirect('/indexK')  # انتقال به صفحه اصلی در صورت عدم دسترسی




def online_meeting(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)

    # بررسی دسترسی
    if appointment.user != request.user and appointment.consultant.user != request.user:
        return redirect('index')

    # دریافت پیام‌ها
    messages = Message.objects.filter(appointment=appointment).order_by('timestamp')

    # نمایش پنل چت فقط اگر وضعیت جلسه 'in_progress' باشد
    if appointment.status == 'in_progress':
        return render(request, 'chat_room.html', {'appointment': appointment, 'messages': messages})
    if appointment.status == 'pending':
        return render(request, 'waiting_for_mentor.html', {'appointment': appointment})
    
    return redirect('/index')

def send_message1(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            Message.objects.create(
                appointment=appointment,
                sender=request.user,
                content=message_content
            )
            return JsonResponse({'success': True})

    return JsonResponse({'error': 'Invalid request'}, status=400)
def nobatk(request):
    # فیلتر کردن نوبت‌هایی که به کاربر تعلق دارند و در حال اجرایند
    active_appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'listnobatman.html', {'active_appointments': active_appointments})
def send_message(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            message = Message.objects.create(
                appointment=appointment,
                sender=request.user,
                content=message_content
            )
            return JsonResponse({'success': True, 'message': message.content, 'sender': request.user.username})

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)      
def consultant_appointments(request):
    consultant = get_object_or_404(information_m, user=request.user)  # یافتن مشاور مرتبط
    appointments = Appointment.objects.filter(consultant=consultant).order_by('-date', '-time')

    return render(request, 'consultant_appointments.html', {
        'consultant': consultant,
        'appointments': appointments
    })

def chat_room(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    
    user_role = 'user' if request.user.is_authenticated and request.user == appointment.user else 'consultant'

    return render(request, 'chat/room.html', {
        'appointment': appointment,
        'user_role': user_role,
        'user': request.user,
        
    })






def start_meeting(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)

    if request.method == 'POST':
        # تغییر وضعیت به in_progress
        appointment.status = 'in_progress'
        appointment.save()

        # هدایت به پنل مشترک
        return redirect('online_meeting', pk=appointment.id)

    
    return JsonResponse({'error': 'Invalid request'}, status=400)
###########################
def join_meeting(request, id):
    appointment = get_object_or_404(Appointment, id=id, user=request.user)
    # منطق برای هدایت کاربر به اتاق جلسه آنلاین
    return render(request, 'chat_room.html', {'appointment': appointment})
