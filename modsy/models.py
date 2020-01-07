from django.db import models
from datetime import datetime




# Create your models here.
# This is the model for rooms
class room(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='images')
    content = models.CharField(max_length=50,default='0000000')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    

    def __str__(self):
    	return self.content

# This is the model for goals   
class goal(models.Model):
	id=models.IntegerField(primary_key=True)
	goal = models.CharField(max_length=50,default='0000000')
	created_at = models.DateTimeField(default=datetime.now)
	updated_at = models.DateTimeField(default=datetime.now)
	
	def __str__(self):
		return self.goal

# This is the model for designs
class design(models.Model):
	id=models.IntegerField(primary_key=True)
	image = models.ImageField(upload_to='images')
	content = models.CharField(max_length=50,default='0000000')
	created_at = models.DateTimeField(default=datetime.now)
	updated_at = models.DateTimeField(default=datetime.now)
	
	
	def __str__(self):
		return self.content

# This is the model for furniture
class furniture(models.Model):
	id=models.IntegerField(primary_key=True)
	phrase=models.CharField(max_length=60,default='111111')
	created_at = models.DateTimeField(default=datetime.now)
	updated_at = models.DateTimeField(default=datetime.now)
	

	def __str__(self):
		return self.phrase

# This is the users model
class user(models.Model):
	username=models.CharField(max_length=20)
	email=models.CharField(max_length=50,unique=True)
	password=models.CharField(max_length=50,default='0000000')
	rooms = models.ForeignKey(room,on_delete=models.CASCADE)
	goals = models.ManyToManyField(goal)
	styles = models.ManyToManyField(design)
	furn = models.ForeignKey(furniture,on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=datetime.now)
	updated_at = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.username
	

