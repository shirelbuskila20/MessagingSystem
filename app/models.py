from django.db import models
from datetime import datetime

# Create your models here.
# class Users(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)

class Message(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    subject= models.CharField(max_length=100)
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    read = models.BooleanField(default=False)