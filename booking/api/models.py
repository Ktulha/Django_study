from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ApiUser(AbstractUser):
  ...


class Hotel(models.Model):
  name=models.CharField(max_length=128)
  
class Room(models.Model):
  num=models.PositiveIntegerField()
  hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="rooms")
  
class Booking(models.Model):
  room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="bookings")
  user=models.ForeignKey(ApiUser,on_delete=models.CASCADE,related_name="bookings") 