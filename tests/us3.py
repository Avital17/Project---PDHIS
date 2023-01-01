from django.test import TestCase , Client
from django.urls import reverse
from ..models import Patient, Event
import datetime

class TestViews(TestCase):
      def test_checkpriority_GET(self):
       client = Client()
       response = client.get(reverse('priority'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'checkpriority.html')


      def test_checkid_POST(self):
       c = Patient.objects.create(identity='111111111')
       self.assertEquals(c.identity, '111111111')
     
       