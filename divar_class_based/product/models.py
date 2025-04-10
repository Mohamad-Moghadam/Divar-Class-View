from django.db import models
from user.models import User


class Product(models.Model):
    name= models.CharField(max_length= 100)
    price= models.BigIntegerField()
    description= models.TextField()
    date_of_publish= models.DateTimeField(auto_now= True)
    seller= models.ForeignKey(User, on_delete=models.PROTECT, related_name= 'seeler_of_each_product')
