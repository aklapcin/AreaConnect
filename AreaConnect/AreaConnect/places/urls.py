from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('AreaConnect.places.views',
    url(r'^$',                             'cities_list',    name='cities_list'),
    url(r'^/(?P<city_slug>[-a-zA-Z0-9]+)/$',      'city_districts_list',    name='city_districts_list'),
    url(r'^(?P<city_slug>[-a-zA-Z0-9]+)/(?P<district_slug>[-a-zA-Z0-9]+)/retails/$',      'district_items',
            kwargs={'item': 'retail'}, name='district_retails'),
    url(r'^/(?P<city_slug>[-a-zA-Z0-9]+)/(?P<district_slug>[-a-zA-Z0-9]+)/services/$',      'district_items',
            kwargs={'item': 'service'}, name='district_services'),
    url(r'^/(?P<city_slug>[-a-zA-Z0-9]+)/(?P<district_slug>[-a-zA-Z0-9]+)/events/$',      'district_items',
            kwargs={'item': 'event'}, name='district_events'),
    url(r'^/(?P<city_slug>[-a-zA-Z0-9]+)/(?P<district_slug>[-a-zA-Z0-9]+)/people/$',      'district_items',
            kwargs={'item': 'people'}, name='district_people'),

    url(r'^(?P<city_slug>[-a-zA-Z0-9]+)/(?P<district_slug>[-a-zA-Z0-9]+)/retails/(?P<item_id>[0-9]+)/$',      'district_item',
            kwargs={'item': 'retail'}, name='district_retail_detail'),
    url(r'^/(?P<city_slug>[-a-zA-Z0-9]+)/(?P<district_slug>[-a-zA-Z0-9]+)/services/(?P<item_id>[0-9]+)/$',      'district_items',
            kwargs={'item': 'service'}, name='district_service_detail'),
    url(r'^/(?P<city_slug>[-a-zA-Z0-9]+)/(?P<district_slug>[-a-zA-Z0-9]+)/events/(?P<item_id>[0-9]+)/$',      'district_items',
            kwargs={'item': 'event'}, name='district_event_detail'),
    url(r'^/(?P<city_slug>[-a-zA-Z0-9]+)/(?P<district_slug>[-a-zA-Z0-9]+)/people/(?P<item_id>[0-9]+)/$',      'district_items',
            kwargs={'item': 'people'}, name='district_people_detail'),


)
