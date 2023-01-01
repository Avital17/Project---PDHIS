
from django.test import TestCase
from ..models import Patient, Event

import datetime



   

class PatientModelTest(TestCase):
        @classmethod
       
        def setUpTestData(cls):
            Patient.objects.create(fname='Moshe', lname='Ron')
        def test_date_created(self):
            patient = Patient.objects.get(id=1)
            self.assertEqual(patient.lname, 'Ron')

class EventModelTest(TestCase):
        @classmethod       

        def setUpTestData(cls):
            Event.objects.create(patient_name='Moshe', doctor_name='Ron', priority=5)

        def test_object_patient_name(self):
            event = Event.objects.get(id=1)
            expected_object_name = f'{event.patient_name}'
            self.assertEqual(str(event), expected_object_name )

        def test_object_doctor_name(self):
            event = Event.objects.get(id=1)
            expected_object_name = f'{event.doctor_name}'
            self.assertNotEqual(event.patient_name, expected_object_name )