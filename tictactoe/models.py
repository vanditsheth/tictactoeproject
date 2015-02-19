from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class player(models.Model):
  user = models.OneToOneField(User)
  name = models.CharField(max_length=10)
  turn = models.IntegerField(default=0)
  def __unicode__(self):
    return self.user.username
  
class moves(models.Model):
  name = models.CharField(max_length=10)
  moves = models.CharField(max_length=9)
  player1 = models.IntegerField(default=0)#0=Nothing, 1=cross won, 2=zero won, 3=tie, 4=Waiting to play again
  player2 = models.IntegerField(default=0)#0=Nothing, 1=cross won, 2=zero won, 3=tie, 4=Waiting to play again
  def __unicode__(self):
    return self.name
  
class messages(models.Model):
  sender = models.CharField(max_length=10)
  message = models.CharField(max_length=500)
  def __unicode__(self):
    return self.sender