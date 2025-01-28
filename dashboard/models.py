from django.db import models
from django_jalali.db.models import jDateField
from django.contrib.auth.models import User


class typem(models.Model):#انواع تخصص
    id=models.AutoField(primary_key=True)  
    name=models.CharField(max_length=100) 
    def __str__(self):
     return self.name   
class typev(models.Model):#انواع مشاوره
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100) 
    def __str__(self):
     return self.name    

class information_m(models.Model):
    id=models.AutoField(primary_key=True)
    namefull=models.CharField(max_length=100)  
    codemeli=models.IntegerField(null=True) 
    datetime = jDateField(null=True)
    jensiyat=models.CharField(max_length=20,null=True)
    mizantahsilat=models.CharField(max_length=100) 
    typemadrak=models.CharField(max_length=100)  
    typetakhasos=models.ManyToManyField(typem)  
    savabeghtahsili=models.CharField(max_length=250)
    savabeghelmi=models.CharField(max_length=250)
    saltajrobe=models.CharField(max_length=250) 
    ostan=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    adress=models.CharField(max_length=250)
    tell=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    imag=models.ImageField(upload_to="files/moshaver")
    zaman=models.IntegerField(null=True)
    online=models.ManyToManyField(typev)
    modat=models.IntegerField(null=True)
    hazine=models.IntegerField(null=True)
    rozhozor=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    biyografi=models.TextField()#درباره ی مشاور
    statu=models.CharField(max_length=20,default='available')
    emtiyaz=models.IntegerField(null=True)#امتیاز
    start_time=models.TimeField( auto_now=False, auto_now_add=False,null=True)
    end_time=models.TimeField(auto_now=False, auto_now_add=False,null=True)
    shomarehesab=models.CharField(max_length=250)
    name_saheb_hesab=models.CharField(max_length=250)
    shaba=models.CharField(max_length=250)
    class Meta:
       verbose_name="مشاوران"

class Appintment(models.Model):
    consultant=models.ForeignKey(information_m,on_delete=models.CASCADE)
    #karbar=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date=models.DateField()
    time=models.TimeField( )
   
    created_at = models.DateTimeField(auto_now_add=True,null=True) 
    class Meta:
       verbose_name="رزرو نوبت"  

class tamas(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    payam=models.TextField()
    ip = models.CharField(max_length=50, null=True)
    tarikh=models.DateTimeField(auto_now_add=True)
    class Meta:
       verbose_name=" نظرات "   
class about(models.Model):
    id=models.AutoField(primary_key=True)
    caption=models.TextField()
    class Meta:
       verbose_name="درباره ی ما  "     
class blog(models.Model):
    id=models.AutoField(primary_key=True) 
    title=models.CharField(max_length=200)
    caption=models.TextField()
    file=models.FileField(upload_to='blog/')
    tarikhenteshar=models.DateField() 
    class Meta:
       verbose_name=" مطالب و وبلاگ"           