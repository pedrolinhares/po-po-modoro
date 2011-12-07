import datetime, random, sha
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
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

			#send email with confirmation link
			email_subject = 'Your account confirmation to po-po-modoro website'
			email_body = "Hello, %s, and thanks for signing up to po-po-modoro website. \
					To activate your account, click this link within 48 hours: \n \
					http://localhost:8000/accounts/confirm/%s" % (new_user.username, 
															new_profile.activation_key)
			send_mail(email_subject, 
					  email_body, 
					  'accounts@po-po-modoro.com', 
					  [new_user.email])

			return render_to_response('register.html', {'created': True},
									context_instance=RequestContext(request))
	else:
		form = RegistrationForm()
	return render_to_response('register.html', {'form': form}, 
						context_instance=RequestContext(request))

def confirm(request, activation_key):
	if request.user.is_authenticated():
		return render_to_response('confirm.html', {'has_account': True})

	user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

	if user_profile.key_expires < datetime.datetime.today():
		render_to_response('confirm.html', {'expired': True})
	
	user_account = user_profile.user
	user_account.is_active = True
	user_account.save()
	
	#authenticate and login user
	user_account.backend = 'django.contrib.auth.backends.ModelBackend'
	login(request, user_account)

	return render_to_response('confirm.html', {'success': True})

