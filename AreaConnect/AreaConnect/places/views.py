from AreaConnect.items.models import Retail, Service, Event, People
from AreaConnect.places.models import City, District
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404


ITEMS_DICT = {
    'retail': Retail,
    'service': Service,
    'event': Event,
    'people': People
}


def cities_list(request, template="places/cities_list.html"):
    cities = City.objects.all()
    ctx = RequestContext(request)
    ctx['cities'] = cities
    return render_to_response(template, {}, context_instance=ctx)


def city_districts_list(request, city_slug=None, template="places/city_districts.html"):
    ctx = RequestContext(request)
    city = get_object_or_404(City, slug=city_slug)
    ctx['city'] = city
    ctx['districts'] = city.districts
    return render_to_response(template, {}, context_instance=ctx)


def district_items(request, city_slug=None, district_slug=None, item=None):
    ctx = RequestContext(request)
    city = get_object_or_404(City, slug=city_slug)
    if district_slug is None:
        raise Http404("Sorry we can't find that")
    districts = city.districts.filter(slug=district_slug)
    if not districts:
        raise Http404("Sorry we can't find that")
    district = districts[0]
    if item is None:
        item = 'retail'
    model = ITEMS_DICT[item]
    items = model.objects.filter(district=district)
    ctx['district'] = district
    ctx['items'] = items
    ctx['events'] = Event.objects.filter(district=district)
    template = "places/district_%s.html" % item
    return render_to_response(template, {}, ctx)


def district_item(request, city_slug=None, district_slug=None, item_id=None, item=None):
    ctx = RequestContext(request)
    city = get_object_or_404(City, slug=city_slug)
    if district_slug is None:
        raise Http404("Sorry we can't find that")
    districts = city.districts.filter(slug=district_slug)
    if not districts:
        raise Http404("Sorry we can't find that")
    district = districts[0]
    if item_id is None or item is None:
        raise Http404("Sorry we can't find that")
    model = ITEMS_DICT[item]
    items = model.objects.filter(district=district).filter(id=item_id)
    if items is None:
        raise Http404("Sorry we can't find that")
    ctx['district'] = district
    ctx['item'] = items[0]
    template = "places/district_%s_detail.html" % item
    return render_to_response(template, {}, ctx)
