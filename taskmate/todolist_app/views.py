from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.template import loader
from datetime import timedelta
from django.contrib.auth.decorators import login_required
import calendar
from calendar import HTMLCalendar
from django.conf import settings
from  django.core.mail import send_mail
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings


today = date.today()
yesterday = today - timedelta(days = 1)

def todolist(request):
    # all_tasks = TaskList.objects.all

    context = {
        'welcome_text':"welcome to PDHIS"
    }
    return render(request,'todolist.html', context)


def about(request):
    return render(request, 'about.html', {})

def doctor(request):
    context = {
        'doctor_text':"welcome doctor"
    }
    return render(request,'login_doctor.html', context)


def patient(request):
    context = {
        'patient_text':"welcome patient"
    }
    return render(request,'patient.html', context)



def secretary(request):
    context = {
        'secretary_text':"welcome secretary"
    }
    return render(request,'secretary.html', context)

@login_required
def hpage(request):
    context = {
        'secretary_text':"welcome"
    }
    return render(request, 'hpage.html', context)

@login_required
def contact(request):
    
    return render(request, 'contact.html', {})

@login_required
def articals(requset):

    return render(requset, 'articals.html',{})


@login_required
def events(request):
    
    return render(request, 'events.html',{})


@login_required
def calendar(requset):

    return render(requset, 'checkdoctorfreetime.html',{})

def checkmyfreetime(request):
    doctor = request.POST['doctor_name']
    freetime = request.POST['date']
    starttime = request.POST['appt-time']
    myemail =  request.POST['email']
   # mydoctor = EventForDoctor.objects.filter(doctor_name=doctor)
    template = loader.get_template('checkfreetime.html')
    context = {
    'doctor': doctor,
    'freetime': freetime,
    'starttime':starttime,
    'myemail':myemail,
    #'mydoctor':mydoctor, 
    }
    return HttpResponse(template.render(context, request)) 



def contactdo(request): 
    if request.method == 'POST':    
         name = request.POST.get("name")
         email = request.POST.get("email")
         message = request.POST.get("message")

         email = EmailMessage(  
            subject= f"{name} from secretary.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email] )

         email.send()


   
    
    context={} 
    return render(request,'massege.html',{}) 


