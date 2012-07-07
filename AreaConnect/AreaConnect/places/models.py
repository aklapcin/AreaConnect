from django.db import models


class City(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class District(models.Model):
    slug = models.SlugField(max_length=50)
    name = models.CharField(max_length=100)
    statment = models.CharField(max_length=500)
    city = models.ForeignKey(City, related_name='districts')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
