from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def isValidUserName(username):
	try:
		User.objects.get(username=username)
	except User.DoesNotExist:
		return
	raise ValidationError('The username "%s" is already taken.' % username)


class RegistrationForm(UserCreationForm):

	username = forms.CharField(label='username',
							max_length=30,
							required=True, validators=[isValidUserName])		
	class Meta:
		model = User 
		fields = ('username','first_name', 'last_name', 'email',)


	def save(self, commit=True):
		new_user = super(RegistrationForm, self).save(commit=False)

		new_user.is_active = False
		
		if commit:
			new_user.save()

		return new_user

