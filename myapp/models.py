from django.db import models

# Create your models here.

class Menu(models.Model):
    id = models.IntegerField(primary_key=True,default=5)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()

class Booking(models.Model):
    id = models.IntegerField(primary_key=True, default=11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    bookingDate = models.DateField()