from django.urls import path
from todolist_app import views




urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('about', views.about, name='about'),
    path('doctor', views.doctor, name='doctor'),
    path('patient', views.patient, name='patient'),
    path('secretary', views.secretary, name='secretary'),
    path('hpage', views.hpage, name='hpage'),
    path('contact', views.contact, name='contact'),
    path('articals', views.articals, name='articals'),
    path('calendar', views.calendar, name='calendar'),
    path('events',views.events, name='events'),
    path('checkmyfreetime/', views.checkmyfreetime, name='checkmyfreetime'),
    
    
    
]