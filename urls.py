from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'insertteamhere.views.home', name='home'),
    # url(r'^insertteamhere/', include('insertteamhere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    #Registration URLs
    url(r'^accounts/', include('registration.urls')),

    #Team App URLs
    url(r'^teams/', include('teams.urls')),
)
