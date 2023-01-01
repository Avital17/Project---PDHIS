

from django.shortcuts import render , redirect
from django.urls import reverse
from django.http import HttpResponse , JsonResponse
from django.template import loader
from .models import Patient, Event, Payment
from datetime import date
from datetime import timedelta
import calendar
from calendar import HTMLCalendar
from django.conf import settings
from  django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.messages import get_messages
from .forms import ContactForm 
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('contactmail.html', {'name':name, 'email':email, 'message':message})
            print('the form was valid')
            send_mail('Scheduling an Appointment', 'message', 'noreply@dianarub8@gmail.com', ['dianarub8@gmail.com'], html_message=html)
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,'trialmail.html',{'form':form})
   


def turnoffalert(request):
    messages.add_message(request,messages.SUCCESS,'THE ALERT WAS TAKEN CARE OFF')
    return render(request,'homemsecretary.html')


def notify(request):
    messages.add_message(request, messages.WARNING,'YOU HAVE A NEW APPOINTMENT')
    return render(request,'notification.html')



def upload(request):
    context = {}
    if request.method =='POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name =  fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'load.html', context)


today = date.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days=1)


def home(request):
    template = loader.get_template('homemsecretary.html')
    return HttpResponse(template.render({}, request ))




def index(request):
    mypatients = Patient.objects.filter(date_created=yesterday)
    template = loader.get_template('listbydates.html')
    context = {
        'mypatients': mypatients,
        'yesterday': yesterday,
    }
    return HttpResponse(template.render(context, request))


def getdoctor(request):
    return render(request, "listbydates.html")


        
def getpatients(request):
    doc= request.GET['doctors']
    newpatients = Patient.objects.filter(doctor=doc, date_created=yesterday)
    return render(request,'listbydoctor.html', { 'newpatients':newpatients, 'doc':doc})


def lists(request):
    Doctorlist = ['Tal', 'Ziv', 'Gart']
    mypatients = Patient.objects.filter(date_created=yesterday)
    template = loader.get_template('listsforalldoctors.html')
    context = {
        'mypatients': mypatients,
        'Doctorlist': Doctorlist,
    }
    return HttpResponse(template.render(context, request))

def checkpriority(request):
    return render(request, "checkpriority.html", {})


def checkid(request):
    ident = request.POST['identity']
    patients = Patient.objects.filter(date_created=yesterday)
    template = loader.get_template('checkid.html')
    context ={
        'patients':patients,
        'ident': ident,
    }
    return HttpResponse(template.render(context, request)) 


def checkdatesofappointments(request):
    cal = HTMLCalendar().formatmonth(today.year, today.month)
    return render(request, 'checkdates.html',{
       
        "cal": cal,}
    )
   

def checkdates(request):
    doctor = request.POST['doctor_name']
    dateappointment = request.POST['date']
    appointments_list = Event.objects.filter(doctor_name=doctor, day=dateappointment )
    template = loader.get_template('tabledates.html')
    context ={
        'doctor': doctor,
        'appointments_list': appointments_list,
        'dateappointment':dateappointment,
    }
    return HttpResponse(template.render(context, request))  

def add (request):
    patients = Patient.objects.all().values()
    events = Event.objects.all().values()
    return render(request, "add.html", {'patients':patients, 'events':events})


def addappointment(request):
    a = request.POST['patient_name']
    b = request.POST['patient_identity']
    x = request.POST['priority']
    d = request.POST['doctor_name']
    e = request.POST['day']
    f= request.POST['start_time']
    g = request.POST['end_time']
    event = Event(patient_name=a, patient_identity=b, priority=x, doctor_name=d, day=e, start_time=f, end_time=g)  
    event.save()
    myevent = Event.objects.filter(doctor_name=d, day=e)
    patient = Patient.objects.filter(identity=b).update(date_appointment=e)
    template = loader.get_template('contact.html')
    context ={
    'a':a,
    'd':d,
    'e':e,
    'f':f,
    }
    return HttpResponse(template.render(context, request))  

def response(request):
    doc1=Event.objects.filter(doctor_name='Tal')
    doc2=Event.objects.filter(doctor_name='Ziv')
    doc3=Event.objects.filter(doctor_name='Gart')
   
    return render(request, "urgent.html", {'doc1':doc1, 'doc2':doc2, 'doc3':doc3,})

def addurgentappointment(request):
    a = request.POST['patient_last_name']
    b = request.POST['patient_identity']
    x = request.POST['priority']
    d = request.POST['doctor_name']
    e = request.POST['day']
    f= request.POST['start_time']
    g = request.POST['end_time']
    h = request.POST['patient_first_name']
    i = request.POST['patient_phone_number']
    m = request.POST['patient_email']
    event = Event(patient_name=a, patient_identity=b, priority=x, doctor_name=d, day=e, start_time=f, end_time=g)  
    event.save()
    patient = Patient(fname=h, lname=a, identity=b, phone=i,
    email=m, date_created=today, date_appointment=e, doctor=d, priority=x,)
    patient.save()
    template = loader.get_template('contact.html')
    context ={
        'd':d,
        'a':a,
        'e':e,
        'f':f,
    }
    return HttpResponse(template.render(context, request))  
    
    
    



def cancel(request):
    patients = Patient.objects.all().values()
    events = Event.objects.all().values()
    template = loader.get_template('cancel.html')
    context ={
    'patients':patients,
    'events':events,
    }
    return HttpResponse(template.render(context, request)) 

def cancellation(request):
    mydoctor = request.POST['doctor_name']
    mydate = request.POST['date']
  
    events = Event.objects.filter(doctor_name=mydoctor, day=mydate)
    events.delete()
    newpatients = Patient.objects.all().values()
    newevents = Event.objects.all().values()
    template = loader.get_template('cancellationsuccess.html')
    context ={
    'newpatients':newpatients,    
    'newevents':newevents,
    }
    return HttpResponse(template.render(context, request)) 

def reschedule (request):
    newevents1 = Event.objects.filter(doctor_name='Tal')
    newevents2 = Event.objects.filter(doctor_name='Ziv')
    newevents3 = Event.objects.filter(doctor_name='Gart')
    template = loader.get_template('reschedule.html')
    context ={
    'newevents1':newevents1,
    'newevents2':newevents2,
    'newevents3':newevents3,
    }
    return HttpResponse(template.render(context, request)) 

def rescheduling(request):
    c = request.POST['identity']
    e = request.POST['date']
    x = request.POST['priority']
    a = request.POST['patient_name']
    d = request.POST['doctor_name']
    f = request.POST['start_time']
    y = request.POST['end_time']
    newevent = Event(patient_name=a, patient_identity=c, priority=x, doctor_name=d, day=e, start_time=f, end_time=y) 
    newevent.save()  
    upevent = Event.objects.filter(doctor_name=d, day=e)
    newpatient = Patient.objects.filter(identity=c)
    newpatient.update(date_appointment=e, doctor=d )
    template = loader.get_template('rescheduler.html')
    context ={
    'newevent':newevent,
    'newpatient':newpatient,
    'upevent':upevent,
    }
    return HttpResponse(template.render(context, request)) 

def payment(request):
    todayevents = Event.objects.filter(day=today)
    return render(request, "payment.html", {'todayevents':todayevents}) 

def confirm(request):
    listpayment = Payment.objects.all().values
    return render(request,'confirm.html', {'listpayment':listpayment})

def tarif(request):
    return render(request,'tarif.html')
 

def contacting(request):
    choice = request.POST['doctors']
    return render(request,'contact1.html', {'choice':choice})