from django.urls import path, re_path
from . import views
app_name='app'
urlpatterns =[
    path('AboutUs', views.AboutUs,name="درباره ما  "),
    path('create_about', views.create_about,name="    ثبت و ذخیره    "),
    path('list_about', views.list_about,name="     لیست   "),
    path('update_about', views.update_about,name="  ویرایش        "),
    path('delet_about', views.delet_about,name="   پاک کردن     "),
    #######################################
    path('Blog',views.Blog,name="وبلاگ    "),
    path('Blogdetails',views.Blogdetails,name="  جزییات وبلاگ    "),
    path('create_blog',views.create_blog,name="    ثبت و ذخیره    "),
    path('list_blog',views.list_blog,name="     لیست   "),
    path('update_blog',views.update_blog,name="  ویرایش"),
    path('delet_blog',views.delet_blog,name="   پاک کردن     "), 
    #########################################################
    
 
    path('ContactUs', views.ContactUs,name="   تماس با ما   "),
    path('contact', views.contact,name="    ثبت و ذخیره    "),
    path('mycomment', views.mycomment,name="    ثبت و ذخیره    "),
    path('update_ContactUs', views.update_ContactUs,name="  ویرایش        "),
    path('delet_ContactUs', views.delet_ContactUs,name="   پاک کردن     "),
    ###################################################
   
 
    
  
    
    path('takhasos', views.takhasos,name="  انواع تخصص ها        "),
    path('nomoshavere', views.nomoshavere,name="      انواع مشاوره ها    "),
    path('savetakhasos', views.savetakhasos,name="       ثبت تخصص ها    "),
    path('savenomoshavere', views.savenomoshavere,name="       ثبت انواع مشاوره    "),
    path('list_filter/<int:pk>', views. list_filter,name="     فیلتر کردن انواع تخصص ها      "),
    ###################################

    
    ]

  
    