from django.urls import path, re_path
from . import views
#app_name='app'
urlpatterns =[
  

    path('submit-reservation/<int:pk>/', views.submit_reservation, name='submit_reservation'),  # ثبت رزرو
    path('online_meeting/<int:pk>/', views.online_meeting, name='online_meeting'),  # پنل آنلاین
    path('appointment-success/<int:pk>/', views.appointment_success, name='appointment_success'),
    path('reservation/<int:pk>/', views.reservation_view, name='reservation'),  # فرم رزرو
    path('start_session/', views.start_session, name='start_session'),
    path('available_times/', views.get_available_times, name='available_times'),  
    path('consultant/appointments/', views.consultant_appointments, name='consultant_appointments'),
    path('appointments/', views.all_appointments, name='all_appointments'),
    #path('nobatk/', views.nobatk, name='nobatk'),
    path('start_meeting/<int:pk>/', views.start_meeting, name='start_meeting'),
    #path('meeting/<int:pk>/', views.online_meeting, name='online_meeting'),
    path('send_message/<int:pk>/', views.send_message, name='send_message'),
    path('listnobatman', views.nobatk, name='listnobatman'),
    path('join_meeting/<int:id>/', views.join_meeting, name='join_meeting'),
    path('chat/<int:pk>/', views.chat_room, name='chat_room'),
]
   

    
    
