# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table('places_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('places', ['City'])

        # Adding model 'District'
        db.create_table('places_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('statment', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(related_name='districts', to=orm['places.City'])),
        ))
        db.send_create_signal('places', ['District'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table('places_city')

        # Deleting model 'District'
        db.delete_table('places_district')


    models = {
        'places.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'places.district': {
            'Meta': {'object_name': 'District'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'districts'", 'to': "orm['places.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'statment': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['places']