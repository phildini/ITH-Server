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
	url(r'^(?P<team_id>\d)/(?P<project_id>\d)/$', 'project'),
        url(r'^(?P<team_id>\d)/(?P<project_id>\d)/edit/$', 'project_edit'),
        url(r'^(?P<team_id>\d)/add/$', 'project_add'),
        url(r'^(?P<team_id>\d)/(?P<project_id>\d)/delete/$', 'project_del'),
)

urlpatterns += staticfiles_urlpatterns()
