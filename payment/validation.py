#from django.core.exceptions import validationError
from .models import payment
class validation():

    def cheekEmpty(self,value):
            if value=="a":
                raise validationError("این کاراکتر مجاز نیست")

    def chekphone(self,value):
            if len(value) <11:
                raise validationError("کمتر از 11 نباشد ")
            if not value.isnumeric():
                raise validationError("باید عدد باشد")
    def chekalpha(self,value):
        if not value.isalpha():
            raise validationError("فقط کاراکتر کجاز می باشد")
    def checkemailexist(self,value):
        result=payment.objects.filter(email=value).all()
        if len(result)>0:
            raise validationError("مقدار تکراری است ")