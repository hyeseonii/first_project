from django.db import models

# Create your models here.
class Cat(models.Model) :

	name=models.CharField(max_length=20, default="unknown")
	age=models.IntegerField(default=0)
	kind=models.CharField(max_length=20, default="unknown")
	image= models.ImageField(upload_to='catimage/',default='catimage/cat1.jpg')

	def __str__(self) :

		return self.name 