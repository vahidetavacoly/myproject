from django.db import models
from app.models import information_m
#from django_jalali.db.models import jDateField
from django.contrib.auth.models import User

class Appintment(models.Model):
    consultant = models.ForeignKey(
        information_m, 
        on_delete=models.CASCADE, 
        related_name="rezerv_appointments"  # جلوگیری از برخورد با اپ دیگر
    )
    karbar = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="rezerv_appointments",  # جلوگیری از برخورد با اپ دیگر
        null=True
    )
    date = models.DateField()
    time = models.TimeField()
    appointment_type = models.CharField(  # افزودن نوع نوبت
        max_length=10,
        choices=[("online", "آنلاین"), ("offline", "حضوری")],
        null=True
    )
    
    def __str__(self):
        return f"Appointment with {self.consultant.namefull} on {self.date} at {self.time}"

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'در انتظار شروع'),
        ('in_progress', 'در حال برگزاری'),
        ('completed', 'پایان یافته'),
        ('cancelled', 'لغو شده'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointments")
    consultant = models.ForeignKey(information_m, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    appointment_type = models.CharField(max_length=20, choices=(('online', 'آنلاین'), ('offline', 'حضوری')))
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # وضعیت جلسه
    
    def __str__(self):
        return f"Appointment with {self.consultant.namefull} on {self.date} ({self.time})" 
class Message(models.Model):
    appointment = models.ForeignKey(Appointment, related_name="messagesaval", on_delete=models.CASCADE,null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  
