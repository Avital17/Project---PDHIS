from django.test import TestCase , Client
from django.urls import reverse
from ..models import Patient, Event
import datetime

class TestViews(TestCase):
    def test_checkdatesofappointments_GET(self):
       client = Client()
       response = client.get(reverse('checkdatesofappointments'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'checkdates.html')

    def test_checkdates_POST(self):
       today = datetime.datetime.now()
       c = Event.objects.create(doctor_name='Tal', day=datetime.datetime.now() )
       self.assertEquals(c.day, today)

       
       