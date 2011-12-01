from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

	user = models.ForeignKey(User, unique=True)
	activation_key = models.CharField(max_length=40)
	key_expires = models.DateTimeField()

	def __unicode__(self):
		return self.user.username
