from twilio.rest import Client
from django.conf import settings
def send_license_code_sms(phone_number, license_code):
    # اطلاعات حساب Twilio
    account_sid = settings.TWILIO_ACCOUNT_SID  # ذخیره‌سازی در تنظیمات (settings)
    auth_token = settings.TWILIO_AUTH_TOKEN  # ذخیره‌سازی در تنظیمات (settings)
    from_number = settings.TWILIO_PHONE_NUMBER  # شماره تلفن Twilio شما

    # ایجاد نمونه از client Twilio
    client = Client(account_sid, auth_token)

    # ارسال پیامک
    message = client.messages.create(
        body=f"کد لایسنس شما: {license_code}",
        from_=from_number,
        to=phone_number
    )

    return message.sid  # شناسه پیامک ارسال‌شده    
def send_sms(phone_number, message_body):
    """
    این تابع برای ارسال پیامک به یک شماره تلفن مشخص استفاده می‌شود.
    """
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message_body,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    if message.sid:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")
class License:
    """
    این کلاس برای مدیریت و اعتبارسنجی کد لایسنس‌ها استفاده می‌شود.
    """
    def __init__(self, code):
        self.code = code

    def is_valid(self):
        # اعتبارسنجی کد لایسنس
        return len(self.code) == 6 and self.code.isdigit()

from datetime import datetime, timedelta

def calculate_expiry_date(days_valid):
    """
    این تابع تاریخ انقضای یک کد لایسنس را محاسبه می‌کند
    که به تعداد روزهای معتبر از تاریخ امروز اضافه می‌شود.
    """
    today = datetime.today()
    expiry_date = today + timedelta(days=days_valid)
    return expiry_date.strftime("%Y-%m-%d")







def validate_license_code(code):
    """
    این تابع برای اعتبارسنجی کد لایسنس استفاده می‌شود.
    """
    # فرض کنید کد لایسنس باید 6 رقم باشد
    if len(code) == 6 and code.isdigit():
        return True
    return False