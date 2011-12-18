from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.pomodoro.views',
    url(r'^$', 					'dashboard'),
    url(r'^inventory/$', 		'inventory'),
    url(r'^todo-today/$', 		'todo_today'),
    url(r'^task/(?P<id>\d+)/$', 'update_task'),
    url(r'^new_task/$', 		'create_task'),
)
