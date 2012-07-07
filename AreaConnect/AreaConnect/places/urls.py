from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('AreaConnect.places.views',
    url(r'^/$',                             'cities_list',    name='cities_list'),
    url(r'^/(?P<city_slug>[-w]+)/$/$',      'city_districts_list',    name='city_districts_list'),
    url(r'^/(?P<city_slug>[-w]+)/(?P<district_slug>[-w]+)/retails/$',      'district_items',
            kwargs={'item': 'retail'}, name='district_retails'),
    url(r'^/(?P<city_slug>[-w]+)/(?P<district_slug>[-w]+)/services/$',      'district_items',
            kwargs={'item': 'service'}, name='district_services'),
    url(r'^/(?P<city_slug>[-w]+)/(?P<district_slug>[-w]+)/events/$',      'district_items',
            kwargs={'item': 'event'}, name='district_events'),
    url(r'^/(?P<city_slug>[-w]+)/(?P<district_slug>[-w]+)/people/$',      'district_items',
            kwargs={'item': 'people'}, name='district_people'),



)
