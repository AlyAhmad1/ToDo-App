from django.db import models
import datetime


class Person(models.Model):
    text = models.CharField(max_length=75)
    # Date = models.DateField(default=str(datetime.datetime.now()).split(' ')[0])
    Date = models.DateField(max_length=75)
    completed = models.BooleanField(default=False)

    def __Str__(self):
        return self.text, self.Date
