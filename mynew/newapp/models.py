from django.db import models

class Person(models.Model):
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=250)

# Create your models here.
