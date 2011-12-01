from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

	username = forms.CharField(label='username',
							max_length=30,
							required=True,) #validators=[self.isValidUserName])		
	class Meta:
		model = User 
		fields = ('username','first_name', 'last_name', 'email',)

#	def isValidUserName(self, field_data, all_data):
#		try:
#			User.objects.get(username=field_data)
#		except User.DoesNotExist:
#			return
#		raise validators.ValidationError('The username "%s" is already taken.' % field_data)

	def save(self, commit=True):
		new_user = super(RegistrationForm, self).save(commit=False)

		new_user.is_active = False
		
		if commit:
			new_user.save()

		return new_user
