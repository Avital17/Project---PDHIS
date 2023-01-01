from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList

def todolist(request):
    all_tasks = TaskList.objects.all


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


def hpage(request):
    context = {
        'secretary_text':"welcome"
    }
    return render(request, 'hpage.html', context)

def contact(request):
    
    return render(request, 'contact.html', {})

def articals(requset):

    return render(requset, 'articals.html',{})
