from django.db import models

# Create your models here.
# Create your models here.
class Flightinfo(models.Model):
    Flightnumber = models.IntegerField()
    Destination = models.CharField(max_length=100)
    #Distance=models.CharField(max_length=100)
    Distance=models.IntegerField()
    Fuelquantity = models.IntegerField()
    #empAddress = models.CharField(max_length=200)

