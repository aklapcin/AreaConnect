from django.db import models
from AreaConnect.places.models import District


class Retail(models.Model):
    district = models.ForeignKey(District)
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    short_desc = models.TextField()
    long_desc = models.TextField()


class Service(models.Model):
    district = models.ForeignKey(District)
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    short_desc = models.TextField()
    long_desc = models.TextField()


class Event(models.Model):
    district = models.ForeignKey(District)
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    short_desc = models.TextField()
    long_desc = models.TextField()
    date = models.DateField()
    place = models.CharField(max_length=300)


class People(models.Model):
    district = models.ForeignKey(District)
    name = models.CharField(max_length=100)
