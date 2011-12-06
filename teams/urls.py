from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('teams.views',
	url(r'^$', 'index'),
	url(r'^(?P<team_id>\d+)/$', 'detail'),
	url(r'^(?P<team_id>\d+)/edit/$', 'edit'),
	url(r'^add/$', 'add'),
	url(r'^about/', 'about'),
	url(r'^(?P<team_id>\d+)/join/$', 'join'),
	url(r'^(?P<team_id>\d+)/delete/$', 'delete'),
)

urlpatterns += staticfiles_urlpatterns()
