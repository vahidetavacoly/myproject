from django.contrib import admin

from .models import payment
#from django.core.exceptions import validationError
from .validation import validation
# Register your models here.
class paymentAdmin(admin.ModelAdmin):

    list_display = ("mablagh","shenase_kharid")
    def formfield_for_dbfield(self, db_field, **kwargs):
        validatio=validation()
        formfild=super().formfield_for_dbfield(db_field,**kwargs)
        if db_field.name=="mablagh":
            formfild.validators.append(validatio.cheekEmpty)
            formfild.validators.append(validatio.chekalpha)
        if db_field.name=="shenase_kharid":
            formfild.validators.append(validatio.checkemailexist)
        """   
        if db_field.name=="phone":
            formfild.validators.append(validation.chekphone)
        """
        return formfild
    def cheekEmpty(self,value):
        if value=="a":
            raise validationError("این کاراکتر مجاز نیست")
"""       
    def chekphone(self,value):
        if len(value) <11:
            raise validationError("کمتر از 11 نباشد ")
        if not value.isnumeric():
            raise validationError("باید عدد باشد")
"""
admin.site.register(payment,paymentAdmin)    