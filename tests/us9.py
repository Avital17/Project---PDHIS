from django.test import TestCase , Client
from django.urls import reverse
from ..models import Patient, Event
import datetime

class TestViews(TestCase):
      def test_payment_GET(self):
       client = Client()
       response = client.get(reverse('payment'))
       self.assertEquals(response.status_code, 200)
       self.assertTemplateUsed(response, 'payment.html')


      def test_confirm_GET(self):    
          client = Client()
          response = client.get(reverse('confirm'))
          self.assertEquals(response.status_code, 200)
          self.assertTemplateUsed(response, 'confirm.html')
     