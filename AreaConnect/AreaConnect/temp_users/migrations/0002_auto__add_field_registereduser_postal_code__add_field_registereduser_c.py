# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'RegisteredUser.postal_code'
        db.add_column('temp_users_registereduser', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(default='0000XX', max_length=20),
                      keep_default=False)

        # Adding field 'RegisteredUser.company_name'
        db.add_column('temp_users_registereduser', 'company_name',
                      self.gf('django.db.models.fields.CharField')(default='Company name', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'RegisteredUser.postal_code'
        db.delete_column('temp_users_registereduser', 'postal_code')

        # Deleting field 'RegisteredUser.company_name'
        db.delete_column('temp_users_registereduser', 'company_name')


    models = {
        'temp_users.registereduser': {
            'Meta': {'object_name': 'RegisteredUser'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['temp_users']