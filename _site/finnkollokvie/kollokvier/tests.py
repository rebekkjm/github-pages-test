from django.test import TestCase
from models import Entry
from django.test.client import Client
import logging

class DBTest(TestCase):
    fixtures = ['mydata']
    c = Client()

    def setUp(self):
        self.rebekka = Entry.objects.create(name="rebekka", subject="inf1100", level="beginner", 
                email="rebekkjm")
        self.tull = Entry.objects.create(name="tull tullesen", subject="tullete", level="0", email="blabla")

    def testEntries(self):
        self.assertEqual(self.rebekka.name, "rebekka")
        self.assertEqual(self.tull.email, "blabla")

    def testcontent(self):
        r = self.c.post('/list/', {'name': 'ola', 'subject': 'inf1010', 'level': 'beginner', 
            'email': 'ola'})
        print r.content
        self.assertTrue('<td>ola</td>' in r.content)

    
