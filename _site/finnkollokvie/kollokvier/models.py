from django.db import models
from django.forms import ModelForm

class Entry(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    #time = models.DateTimeField()
    email = models.CharField(max_length=200)
    level = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class EntryForm(ModelForm):
    class Meta:
        model = Entry

#class Level?
