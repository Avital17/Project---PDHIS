from django.test import TestCase , Client
from django.urls import reverse
from ..models import Patient, Event
import datetime

class TestViews(TestCase):
      def test_reschedule_GET(self):
       client = Client()
       response = client.get(reverse('reschedule'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'reschedule.html')


      def test_rescheduling_POST(self):
        today = datetime.datetime.now()
        c = Event.objects.create(day=datetime.datetime.now())
        self.assertEquals(c.pk, 1)
     