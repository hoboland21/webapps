from django.db import models

# Create your models here.
class States(models.Model) :
  abbrev        = models.CharField(max_length=6)
  name 			= models.CharField(max_length=40,blank=True)
  population	= models.IntegerField(default=0)
  url  			= models.CharField(max_length=256,blank=True)
