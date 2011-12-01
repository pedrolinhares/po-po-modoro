import datetime, random, sha
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.user_app.models import UserProfile
from apps.user_app.forms import RegistrationForm

def register(request):
	if request.user.is_authenticated():
		return render_to_response('register.html', {'has_account': True})
	
	if request.method == 'POST':
		form = RegistrationForm(request.POST, request.FILES)
		
		if form.is_valid():
			new_user = form.save(commit=True)

			#build activation_key for the new account
			salt = sha.new(str(random.random())).hexdigest()[:5]
			activation_key = sha.new(salt+new_user.username).hexdigest()
			key_expires = datetime.datetime.today() + datetime.timedelta(2)

			new_profile = UserProfile(user=new_user,
									  activation_key=activation_key,
									  key_expires=key_expires)
			new_profile.save()

			return render_to_response('register.html', {'created': True},
									context_instance=RequestContext(request))
	else:
		form = RegistrationForm()
	return render_to_response('register.html', {'form': form}, 
						context_instance=RequestContext(request))
