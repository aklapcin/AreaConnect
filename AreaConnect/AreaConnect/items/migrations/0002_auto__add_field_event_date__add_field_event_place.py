# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.date'
        db.add_column('items_event', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 7, 8, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.place'
        db.add_column('items_event', 'place',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=300),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.date'
        db.delete_column('items_event', 'date')

        # Deleting field 'Event.place'
        db.delete_column('items_event', 'place')


    models = {
        'items.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_desc': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'short_desc': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'items.people': {
            'Meta': {'object_name': 'People'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'items.retail': {
            'Meta': {'object_name': 'Retail'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_desc': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_desc': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'items.service': {
            'Meta': {'object_name': 'Service'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_desc': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_desc': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
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

    complete_apps = ['items']