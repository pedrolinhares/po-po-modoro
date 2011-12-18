from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
        url(r'^', include('apps.pomodoro.urls')),
        url(r'^accounts/', include('apps.user_app.urls')),
        url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
