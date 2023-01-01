from django.test import TestCase , Client
from django.urls import reverse
from ..models import Patient, Event
import datetime

class TestViews(TestCase):
      def test_add_GET(self):
       client = Client()
       response = client.get(reverse('add'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'add.html')


      def test_addappointments_POST(self):
        today = datetime.datetime.now()
        c = Event.objects.create(day=datetime.datetime.now())
        self.assertEquals(c.day, today)
     