            

from django.test import TestCase , Client
from django.urls import reverse
from ..models import Patient, Event
import datetime

class TestViews(TestCase):
   def test_getdoctor_GET(self):
       client = Client()
       response = client.get(reverse('getdoctor'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'listbydates.html')

   def test_getpatients_POST(self):
       c = Patient.objects.create(doctor='Tal')
       self.assertEquals(c.doctor, 'Tal')
       


