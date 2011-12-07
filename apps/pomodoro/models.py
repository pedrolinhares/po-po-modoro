from django.db import models
from apps.user_app.models import UserProfile

class Task(models.Model):
	"""Tasks are units of work measured in terms of
	   pomororos."""
	title = models.CharField(max_length=100)
	pomodoros = models.IntegerField()
	worksheet = models.CharField(max_length=50)
	user = models.ForeignKey(UserProfile)

