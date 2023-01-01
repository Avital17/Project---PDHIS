from django.test import TestCase , Client
from django.urls import reverse
from ..models import Patient, Event
import datetime

class TestViews(TestCase):
      def test_cancel_GET(self):
       client = Client()
       response = client.get(reverse('cancel'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'cancel.html')


      def test_cancellation_POST(self):
        today = datetime.datetime.now()
        c = Event.objects.create(day=today, doctor_name='Tal')
        c.delete()
        self.assertEquals(c.pk, None)