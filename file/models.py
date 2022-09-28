from email.policy import default
from django.db import models
import datetime

class  Uploadfile(models.Model):
    title  = models.CharField(max_length=100,default="New Document" ,blank=True)
    file  = models.FileField(upload_to='ImageFiles')
    img  = models.FileField(upload_to='ImageFiles')
    date = models.DateTimeField(default=datetime.datetime.today())
    desc = models.TextField(default="")

    def __str__(self):
        return self.title


def filesize(file):
    x = file.size
    y = 512000
    if x < y:
        value = round(x/1000, 2)
        ext = ' kb'
    elif x < y*1000:
        value = round(x/1000000, 2)
        ext = ' Mb'
    else:
        value = round(x/1000000000, 2)
        ext = ' Gb'
    return str(value)+ext