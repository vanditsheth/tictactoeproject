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
  def __unicode__(self):
    return self.name
