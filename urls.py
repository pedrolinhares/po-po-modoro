from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	# TODO: move this urls to pomodoro app
	(r'^$', 'apps.pomodoro.views.dashboard'),
	(r'^inventory/$', 'apps.pomodoro.views.inventory'),
	(r'^todo-today/$', 'apps.pomodoro.views.todo_today'),

	# TODO: move this url to user_app app
	(r'^register/$', 'apps.user_app.views.register'),

	(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
	(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        {'login_url': '/login/'}),
)

