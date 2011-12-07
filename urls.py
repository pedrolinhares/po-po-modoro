from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
        url(r'^', include('apps.pomodoro.urls')),
        url(r'^accounts/', include('apps.user_app.urls')),
)
