from django.db import models
from django.core.exceptions import ValidationError
import datetime
from django.urls import reverse


class Patient(models.Model):

    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=20)
    identity = models.CharField(max_length=9)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    date_created = models.DateField(auto_now=False,auto_now_add=True)
    date_appointment = models.DateField(auto_now=True,auto_now_add=False)
    doctor = models.CharField(max_length=20)
    priority = models.IntegerField(null=True)

    def __str__(self):
        return self.doctor

class Meta:
    ordering = ['-date_created']

class Event(models.Model):
    day = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    patient_name = models.CharField(max_length=20)
    patient_identity = models.CharField(max_length=9)
    doctor_name = models.CharField(max_length=20)
    priority = models.IntegerField(null=True)

    def __str__(self):
        return self.patient_name
    

class Meta:
    verbose_name = u'Scheduling'
    verbose_name_plural = u'Scheduling'

class Document(models.Model):
    Document = models.FileField(upload_to='uploads')

class Payment(models.Model):
     patient_name = models.CharField(max_length=20)
     patient_identity = models.CharField(max_length=9)
     patient_payment = models.IntegerField(null=True)



def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
    overlap = False
    if new_start == fixed_end or new_end == fixed_start:
        overlap = False
    elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_start):
        overlap = True
    elif new_start <= fixed_start and new_end >= fixed_end:
         overlap = True

    return overlap

def get_absolute_url(self):
    url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
    return u'<a href="%s">%s</a>' % (url, str(self.start_time))

def clean(self):
    if self.end_time <= self.start_time:
        raise ValidationError(' Ending times after starting times')
    events = Event.objects.filter(day=self.day)
    if events.exists():
        for event in events:
            if self.check.overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                raise ValidationError('There is an overlap with another event:'+ str(event.day)+','+ str(event.start_time) + '-' + str(event.end_time))

