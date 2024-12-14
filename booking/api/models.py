from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ApiUser(AbstractUser):
  ...


class Hotel(models.Model):
  name=models.CharField(max_length=128)
  
  def __str__(self):
    return f'{self.id}: {self.name}'
  
class Room(models.Model):
  num=models.PositiveIntegerField()
  hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="rooms")
  
  def __str__(self):
    return f'{self.hotel.name}. Room num:  {self.num}'
  
class Booking(models.Model):
  room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="bookings")
  user=models.ForeignKey(ApiUser,on_delete=models.CASCADE,related_name="bookings") 
  
