from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.pomodoro.views.dashboard'),
    url(r'^inventory/$', 'apps.pomodoro.views.inventory'),
    url(r'^todo-today/$', 'apps.pomodoro.views.todo_today'),
)
