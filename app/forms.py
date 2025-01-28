from django import forms
from django_jalali.forms import jDateField,jDateTimeField
from django_jalali.admin.widgets import AdminjDateWidget,AdminSplitjDateTime
from .models import typev,typem,padcast,test,question,answer,image,vidio
from datetime import datetime
from django.core.exceptions import ValidationError
class login_f(forms.Form):
    def __init__(self,*args,**kwargs):
        super(login_f,self).__init__(*args,**kwargs)
        for item in login_f.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
    username=forms.CharField(required=True,label="نام کاربری ")
    password=forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput)
class singup_f(forms.Form):
    def __init__(self,*args,**kwargs):
        super(singup_f,self).__init__(*args,**kwargs)
        for item in singup_f.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
    namefull = forms.CharField(required=True, label=" نام و نام خانوادگی ")
    username=forms.CharField(required=True,label="نام کاربری ",)
    password=forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput)
    email=forms.EmailField(required=True,label="ایمیل ")
    tell=forms.IntegerField(required=True,label="تلفن ")
    id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")

     
class typem_f(forms.Form):#انواع تخصص
    
    name=forms.CharField(required=True,label="     انواع تخصص ها    ",widget=forms.TextInput(attrs={'class':'form-control'},))    
class typev_f(forms.Form):#انواع مشاوره

    name=forms.CharField(required=True,label="    انواع مشاوره ها     ",widget=forms.TextInput(attrs={'class':'form-control'},))        
class information_m_f(forms.Form):#عضویت مشاوره در سایت
 
    namefull=forms.CharField(required=True,label="    نام و نام خانوادگی  ",widget=forms.TextInput(attrs={'class':'form-control'}))  
    codemeli=forms.IntegerField(required=True,label="    کد ملی ",widget=forms.NumberInput(attrs={'class':'form-control'})) 
    
    datetime = jDateField(widget=AdminjDateWidget(),label="تاریخ تولد")
    CHOICES=(('option1',' اقا'),('option2','خانم'))
    jensiyat=forms.ChoiceField(choices=CHOICES,required=True,label="    جنسیت     ",widget=forms.Select(attrs={'class':'form-control'}))
    mizantahsilat=forms.CharField(required=True,label="   میزان تحصیلات      ",widget=forms.TextInput(attrs={'class':'form-control'}))  
    typemadrak=forms.CharField(required=True,label="     نوع مدرک    ",widget=forms.TextInput(attrs={'class':'form-control'}))  
    typetakhasos=forms.ModelMultipleChoiceField(queryset=typem.objects.all(),widget=forms.CheckboxSelectMultiple,required=True,label=" نوع تخصص")  
    savabeghtahsili=forms.CharField(required=True,label="   سوابق تحصیلی      ",widget=forms.TextInput(attrs={'class':'form-control'}))
    savabeghelmi=forms.CharField(required=True,label="     سوابق علمی    ",widget=forms.TextInput(attrs={'class':'form-control'}))
    saltajrobe=forms.CharField(required=True,label="      چند سال تجربه کار دارید   ",widget=forms.TextInput(attrs={'class':'form-control'})) 
    ostan=forms.CharField(required=True,label="    استان     ",widget=forms.TextInput(attrs={'class':'form-control'}))
    city=forms.CharField(required=True,label="  شهر       ",widget=forms.TextInput(attrs={'class':'form-control'}))
    adress=forms.CharField(required=True,label="    ادرس محل کار     ",widget=forms.TextInput(attrs={'class':'form-control'}))
    tell=forms.IntegerField(required=True,label="     شماره تماس    ",widget=forms.NumberInput(attrs={'class':'form-control'}))
    imag=forms.ImageField(required=True,label="    عکس پروفایل     ")
    zaman=forms.IntegerField(required=True,label="    تلفن محل کار  ",widget=forms.NumberInput(attrs={'class':'form-control'}))
    online=forms.ModelMultipleChoiceField(queryset=typev.objects.all(),widget=forms.CheckboxSelectMultiple,required=True,label=" نوع مشاوره")  
    modat=forms.IntegerField(required=True,label="  مدت زمان هر جلسه به دقیقه       ",widget=forms.NumberInput(attrs={'class':'form-control'}))
    hazine=forms.IntegerField(required=True,label="    هزینه هر جلسه به تومان     ",widget=forms.NumberInput(attrs={'class':'form-control'}))
    rozhozor=forms.CharField(required=True,label="   روزهای نوبت دهی حضوری     ",widget=forms.TextInput(attrs={'class':'form-control'}))
    rozonline=forms.CharField(required=True,label="   روزهای نوبت دهی انلاین     ",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True,label="    ایمیل     ",widget=forms.EmailInput(attrs={'class':'form-control'}))
    biyografi=forms.CharField(required=True,label="   درباره خودتان     ",widget=forms.TextInput(attrs={'class':'form-control'}))#درباره ی مشاور
    start_time=forms.TimeField(required=True,label="   شروع ساعت کاری ",widget=forms.TimeInput(attrs={'type':'time'}))
    end_time=forms.TimeField(required=True,label="   پایان ساعت کاری ",widget=forms.TimeInput(attrs={'type':'time'}))
    id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")



class padcast_f(forms.Form):
     title = forms.CharField(required=True,label="   عنوان ",widget=forms.TextInput(attrs={'class':'form-control'},))
     caption = forms.CharField(required=True,label="توضیحات ",widget=forms.TextInput(attrs={'class':'form-control'}))
     audio = forms.FileField(required=True,label="فایل")
    
     id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
  
    
    
class test_f(forms.Form):
     name = forms.CharField(required=True,label= "نام"   ,widget=forms.TextInput(attrs={'class':'form-control'},))
     soal = forms.CharField(required=True,label=" سوالات",widget=forms.TextInput(attrs={'class':'form-control'}))
     result = forms.CharField(required=True,label=" نتیجه",widget=forms.TextInput(attrs={'class':'form-control'}))
     id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
     
     class Meta:
        model =test 
        fields = ("نتیجه","سوالات ","نام ")

   

    
class tamas_f(forms.Form):
    def __init__(self,*args,**kwargs):
        super(tamas_f,self).__init__(*args,**kwargs)
        for item in tamas_f.visible_fields(self):
            item.field.widget.attrs["class"]="form-control"
    name=forms.CharField(required=True,label="نام کامل")
    email=forms.EmailField(required=True,label="ایمیل")
    payam = forms.CharField(required=True, label="پیام ")
    id= forms.CharField(widget=forms.HiddenInput,required=True,initial="0",label="")   
class about_f(forms.Form):
     caption = forms.CharField(required=True,label="متن    ",widget=forms.TextInput(attrs={'class':'form-control'},)) 
class question_f(forms.Form):
    title = forms.CharField(required=True,label="عنوان",widget=forms.TextInput(attrs={'class':'form-control'},))
    caption = forms.CharField(required=True,label=" محتوا",widget=forms.TextInput(attrs={'class':'form-control'}))
    id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
   
   
     
    
class answer_f(forms.Form):
   
      caption = forms.CharField(required=True,label="پاسخ",widget=forms.TextInput(attrs={'class':'form-control'},))
      id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
     
    
   
     
class image_f(forms.Form):
      title = forms.CharField(required=True,label="عنوان    ",widget=forms.TextInput(attrs={'class':'form-control'},))
      img = forms.FileField(required=True,label="عکس ")
      id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
  
     
class vidio_f(forms.Form):
      title = forms.CharField(required=True,label="عنوان    ",widget=forms.TextInput(attrs={'class':'form-control'},))
      video = forms.FileField(required=True,label="ویدیو ")
      id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
     
      class Meta:
        model =vidio 
        fields = ("ویدیو","عنوان")
        labels={'ویدیو':'ویدیو','عنوان':'عنوان'}
class blog_f(forms.Form):
     title = forms.CharField(required=True,label="   عنوان ",widget=forms.TextInput(attrs={'class':'form-control'},))
     caption = forms.CharField(required=True,label="توضیحات ",widget=forms.TextInput(attrs={'class':'form-control'}))
    
     
     id = forms.IntegerField(required=True, label=" ", widget=forms.HiddenInput(),initial="0")
class usertype_f(forms.Form):
    USER_TyPES=[('client',"کاربر"),('moshaver',"مشاور")]
    user_type=forms.ChoiceField(label="به عنوان :",choices=USER_TyPES,widget=forms.RadioSelect)     
class LicenseForm(forms.Form):
    license_code = forms.CharField(max_length=20, required=True, label='کد لایسنس')
    document = forms.FileField(required=True, label='مدارک')
