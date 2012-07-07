from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'AreaConnect.views.home', name='home'),
    url(r'^places/', include('AreaConnect.places.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
