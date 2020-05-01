from django.db import models

# Create your models here.
class States(models.Model) :
	abbrev        = models.CharField(max_length=6)
	name 			= models.CharField(max_length=40,blank=True)
	population	= models.IntegerField(default=0)
	url  			= models.CharField(max_length=256,blank=True)



class Countries(models.Model) :
	abbrev        = models.CharField(max_length=6)
	name 			= models.CharField(max_length=40,blank=True)
	population	= models.IntegerField(default=0)
	ranking		= models.IntegerField(default=0)
	url  			= models.CharField(max_length=256,blank=True)


class StateData(models.Model) :
	states      = models.ForeignKey(States, on_delete=models.CASCADE)
	timestamp 	= models.IntegerField(default=0)
	tested 		= models.IntegerField(default=0)
	positive	= models.IntegerField(default=0)
	deaths		= models.IntegerField(default=0)