from django.contrib import admin
from .models import information_m,typem,typev,tamas,blog,about
# Register your models here.
@admin.register(information_m)
class consultantAdmin(admin.ModelAdmin):
    listdisplay=('title','',)
    search=('title')
@admin.register(typem)
class typemAdmin(admin.ModelAdmin):
    listdisplay=('name','',)
    search=('name')
@admin.register(typev)
class typevAdmin(admin.ModelAdmin):
    listdisplay=('name','',)
    search=('name')
#@admin.register(Appintment)
#class AppintmentAdmin(admin.ModelAdmin):
 #   listdisplay=('consultant','',)
  #  search=('consultant')
#@admin.register(payment)
#class paymentAdmin(admin.ModelAdmin):
   # listdisplay=('consultant','',)
    #search=('consultant')
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