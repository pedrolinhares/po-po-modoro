from django.test import TestCase
from should_dsl import should
from apps.user_app.models import UserProfile
from django.core.exceptions import ValidationError

class UserProfileTests(TestCase):
	def test_access_registration_form(self):
		resp = self.client.get('/register/')
		resp.status_code | should | equal_to(200) 

	def test_user_creation(self):
		UserProfile.objects.count() | should | equal_to(0)

		resp = self.client.post('/register/', {'username': 'foo', 
											   'first_name': 'xunda',
											   'last_name':'foo_bar', 
											   'email': 'foo@bar.com', 
											   'password1': 'lapela',
											   'password2': 'lapela'})
		resp.status_code | should | equal_to(200) 
		
		UserProfile.objects.count() | should | equal_to(1)

	def test_duplicated_username_should_not_be_created(self):
		resp_1 = self.client.post('/register/', {'username': 'foo', 
											   'first_name': 'xunda',
											   'last_name':'foo_bar', 
											   'email': 'foo@bar.com', 
											   'password1': 'lapela',
											   'password2': 'lapela'})

		resp_2 = self.client.post('/register/', {'username': 'foo', 
											   'first_name': 'someth',
											   'last_name':'bar_foo', 
											   'email': 'foo@bar.com', 
											   'password1': 'xunda',
											   'password2': 'xunda'})
		resp_2.content | should | include('The username &quot;foo&quot; is already taken.')

		UserProfile.objects.count() | should | equal_to(1)
