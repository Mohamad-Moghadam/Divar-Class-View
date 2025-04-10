from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    name = models.CharField(max_length=100)
    number = PhoneNumberField()
    location= models.TextField()
    national_id= models.PositiveIntegerField(unique= True)
