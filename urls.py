from django.urls import path
from .import views



from .import admin

urlpatterns = [
     path('', views.home, name='home'),
     path('index/', views.index, name='index'),
     path('getdoctor/', views.getdoctor, name='getdoctor'),
     path('getpatients/', views.getpatients, name='getpatients'),
     path('lists/', views.lists, name='lists'),
     path('checkpriority/', views.checkpriority, name='priority'),
     path('checkpriority/checkid/', views.checkid, name='checkid'),
    # path('admin:events_event_changelist', admin.changelist_view, name='changeview')
     path('checkdatesofappointments/', views.checkdatesofappointments, name='checkdatesofappointments'),
     path('checkdatesofappointments/checkdates/', views.checkdates, name='checkdates'),
     path('add/', views.add, name='add'),
     path('add/addappointment/', views.addappointment, name='addappointment'),
     path('response/', views.response, name='response'),
     path('response/addurgentappointment/', views.addurgentappointment, name='addurgentappointment'),
     path('turnoffalert', views.turnoffalert, name='turnoffalert'),
     path('cancel/', views.cancel, name='cancel'),
     path('cancel/cancellation/', views.cancellation, name='cancellation'),
     path('reschedule/', views.reschedule, name='reschedule'),
     path('reschedule/rescheduling/', views.rescheduling, name='rescheduling'),
     path('payment/', views.payment, name='payment'),
     path('contact/', views.contact, name='contact'),
     path('notify/', views.notify, name='notify'),
     path('upload/', views.upload, name='upload'),
     path('confirm/', views.confirm, name='confirm'),
     path('tarif/', views.tarif, name='tarif'),
        path('tarif/contacting/', views.contacting, name='contacting'),
     
    
   
    
     
    



   

]   
