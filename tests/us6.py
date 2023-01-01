from django.test import TestCase , Client
from django.urls import reverse
from ..models import Patient, Event
import datetime

class TestViews(TestCase):
      def test_response_GET(self):
       client = Client()
       response = client.get(reverse('response'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'urgent.html')


      def test_addurgentappointment_POST(self):
        today = datetime.datetime.now()
        c = Event.objects.create(day=datetime.datetime.now())
        self.assertEquals(c.day, today)
     

      def test_contact_GET(self):
       client = Client()
       response = client.get(reverse('contact'))
       self.assertTemplateUsed(response, 'trialmail.html')