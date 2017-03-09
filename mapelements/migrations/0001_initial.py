# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MapPoint'
        db.create_table(u'mapelements_mappoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('type_of_point', self.gf('django.db.models.fields.CharField')(default='default', max_length=255)),
            ('coordinates', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=1000, blank=True)),
            ('is_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'mapelements', ['MapPoint'])


    def backwards(self, orm):
        # Deleting model 'MapPoint'
        db.delete_table(u'mapelements_mappoint')


    models = {
        u'mapelements.mappoint': {
            'Meta': {'object_name': 'MapPoint'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type_of_point': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '255'})
        }
    }

    complete_apps = ['mapelements']