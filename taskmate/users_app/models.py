from django.db import models
from django.contrib.auth.models import User

# Create your models here

#יצרנו מודל לדוקטור שיורש מהיוזר שדגאנגו מספק לנו(30)
class UserDoctor(models.Model):
    user_doctor = models.OneToOneField(User, on_delete=models.CASCADE)
    Role = models.CharField(max_length=1, choices=(('1', 'doctor'),('1', 'doctor')), default='doctor')
    department = models.CharField(max_length=50, choices = (('1','Otorhinolaryngology'),('2', 'Cardiology'),('3','Oncology'),('4','Dermatologist'),('5','Endocrinologist'),('6','Gastroenterologist'),('7','Hematologist'),('8','Nephrologists'),('9','Neurologists'),('10','Ophthalmologist')))
   
    def __str__(self):
        return self.user_doctor.username

