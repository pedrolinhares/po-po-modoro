from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',

    url(r'^register/$', 'apps.user_app.views.register'),
	url(r'^confirm/(?P<activation_key>\w+)/$', 'apps.user_app.views.confirm'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        {'login_url': '/accounts/login/'}),
)
