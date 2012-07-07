# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RegisteredUser'
        db.create_table('temp_users_registereduser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('temp_users', ['RegisteredUser'])


    def backwards(self, orm):
        # Deleting model 'RegisteredUser'
        db.delete_table('temp_users_registereduser')


    models = {
        'temp_users.registereduser': {
            'Meta': {'object_name': 'RegisteredUser'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['temp_users']