from django.contrib import admin
from .models import typem,typev,information_m,Appintment,tamas,about,blog


# Register your models here.
@admin.register(information_m)
class information_mAdmin(admin.ModelAdmin):
    listdisplay=('namefull','',)
    search=('namefull')
@admin.register(typem)
class typemAdmin(admin.ModelAdmin):
    listdisplay=('name','',)
    search=('name')
@admin.register(typev)
class typevAdmin(admin.ModelAdmin):
    listdisplay=('name','',)
    search=('name')
@admin.register(Appintment)
class AppintmentAdmin(admin.ModelAdmin):
    listdisplay=('consultant','',)
    search=('consultant')
#@admin.register(payment)
#class paymentAdmin(admin.ModelAdmin):
   # listdisplay=('consultant','',)
   # search=('consultant')
@admin.register(tamas)
class tamasAdmin(admin.ModelAdmin):
    listdisplay=('email','',)
    search=('email')
@admin.register(about)
class aboutAdmin(admin.ModelAdmin):
    listdisplay=('caption','',)
    search=('caption')
@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    listdisplay=('title','',)
    search=('title')                            
# Register your models here.
#@admin.sit.register(User)
#class UserAdmin(admin.ModelAdmin):
    #List_display=('namefull')
    #admin.sit.register(User.UserAdmin)
#@admin.register(information_m)
#class information_mAdmin(admin.ModelAdmin):
    #list_display=(' tell','email',' namefull    ',)
    #search_fields=('email',' namefull  ',)
    #admin.register(information_m.information_mAdmin)#ثبت مدل به وسیله ادمین سایت رجیستر
#@admin.register(typev)
##class typevAdmin(admin.ModelAdmin):
    #list_display=[' name ']
    #search_fields=[' name']
    #admin.register(typev.name)
#@admin.register(typem)
#class typemAdmin(admin.ModelAdmin):
    #list_display=[' name ']
    #search_fields=[' name']
    #admin.register(typem.name)

#@admin.register(Appintment)
#class AppintmentAdmin(admin.ModelAdmin):
    #list_display=('  date ','time')
    #search_fields=('consultant   ',)
    #admin.register(Appintment.time)


##@admin.register(payment)
#class paymentAdmin(admin.ModelAdmin):
    #list_display=[' mablagh']

   # def custom(self,obj):
        #return f"{obj.mablagh}" 
    #custom.short_description ='مبلغ'
    #search_fields=(' consultant ',)
    #admin.register(payment.mablagh)

# Register your models here.

