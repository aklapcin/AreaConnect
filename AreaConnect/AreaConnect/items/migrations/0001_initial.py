# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Retail'
        db.create_table('items_retail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.District'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_desc', self.gf('django.db.models.fields.TextField')()),
            ('long_desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('items', ['Retail'])

        # Adding model 'Service'
        db.create_table('items_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.District'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_desc', self.gf('django.db.models.fields.TextField')()),
            ('long_desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('items', ['Service'])

        # Adding model 'Event'
        db.create_table('items_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.District'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_desc', self.gf('django.db.models.fields.TextField')()),
            ('long_desc', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('items', ['Event'])

        # Adding model 'People'
        db.create_table('items_people', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.District'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('items', ['People'])


    def backwards(self, orm):
        # Deleting model 'Retail'
        db.delete_table('items_retail')

        # Deleting model 'Service'
        db.delete_table('items_service')

        # Deleting model 'Event'
        db.delete_table('items_event')

        # Deleting model 'People'
        db.delete_table('items_people')


    models = {
        'items.event': {
            'Meta': {'object_name': 'Event'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['places.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_desc': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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