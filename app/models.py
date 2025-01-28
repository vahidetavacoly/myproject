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
class padcast(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True) 
    title=models.CharField(max_length=200)
    caption=models.TextField()
    audio=models.FileField(upload_to='files/padcast')
    tarikhenteshar=models.DateTimeField(auto_now_add=True,null=True)
class test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
   

    name=models.CharField(max_length=100)
    soal=models.TextField()
    result=models.CharField(max_length=100,null=True,blank=True) 
class image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
    
    title=models.CharField(max_length=200)
    img=models.FileField(upload_to='imag/')
    zaman_bargozary=models.DateTimeField(auto_now_add=True)
class vidio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
   
    title=models.CharField(max_length=200)
    video=models.FileField(upload_to='vidio/')
    zaman_bargozary=models.DateTimeField(auto_now_add=True)              
class information_m(models.Model):
    #عضویت مشاوره در س
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='consultant')
    id=models.AutoField(primary_key=True)
    codemeli = models.CharField(max_length=10, unique=True)  # تعیین کد ملی به عنوان یکتا
    email = models.EmailField(unique=True)  # ایمیل باید یکتا باشد
    namefull=models.CharField(max_length=100)  
   
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
    rozonline=models.CharField(max_length=250,null=True)
    biyografi=models.TextField()#درباره ی مشاور
    statu=models.CharField(max_length=20,default='available')
    emtiyaz=models.IntegerField(null=True)#امتیاز
    start_time=models.TimeField( auto_now=False, auto_now_add=False,null=True)
    end_time=models.TimeField(auto_now=False, auto_now_add=False,null=True)
    
class sabtkarbar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
class tamas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    payam=models.TextField()
    ip = models.CharField(max_length=50, null=True)
    tarikh=models.DateTimeField(auto_now_add=True) 
class about(models.Model):
    id=models.AutoField(primary_key=True)
    caption=models.TextField()
class question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    caption=models.TextField()
    tarikh=models.DateTimeField(auto_now_add=True)
    berozresani=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,default='پاسخ داده شد',null=True)
class answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    id=models.AutoField(primary_key=True)
    soal=models.ForeignKey(question,on_delete=models.CASCADE,related_name='answer')
    caption=models.TextField()
    tarikh=models.DateTimeField(auto_now_add=True)
    berozresani=models.DateTimeField(auto_now_add=True)
class blog(models.Model):
    id=models.AutoField(primary_key=True) 
    title=models.CharField(max_length=200)
    caption=models.TextField()
    file=models.FileField(upload_to='blog/')
    tarikhenteshar=models.DateField()  
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username  
class Profile(models.Model):
    ROLE_CHOICES = (
        ('client', 'کاربر عادی'),
        ('moshaver', 'مشاور'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')          
    def __str__(self):
        return f"{self.user.username} - {self.role}"