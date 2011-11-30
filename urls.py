from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'apps.home_page.views.show_index'),
	(r'^login/$', 'django.contrib.auth.views.login', 
				 {'template_name': 'login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
				  {'login_url': '/login/'}),
)
