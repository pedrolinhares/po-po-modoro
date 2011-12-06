from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# TODO: move this urls to home_page app
	(r'^$', 'apps.home_page.views.dashboard'),
	(r'^inventory/$', 'apps.home_page.views.inventory'),
	(r'^todo-today/$', 'apps.home_page.views.todo_today'),

	# TODO: move this url to user_app app
	(r'^register/$', 'apps.user_app.views.register'),

	(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        {'login_url': '/login/'}),
)

