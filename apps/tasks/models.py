from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
	"""Tasks are units of work measured in terms of
	   pomororos."""
	WORKSHEETS = (
			('0', 'none'), 
			('1', 'inventory'), 
			('2', 'todo'))	
	title = models.CharField(max_length=100)
	num_pomodoros = models.IntegerField()
	worksheet = models.CharField(max_length=100, choices=WORKSHEETS)
	user = models.ForeignKey(User)
