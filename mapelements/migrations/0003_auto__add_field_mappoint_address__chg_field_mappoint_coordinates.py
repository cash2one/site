# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MapPoint.address'
        db.add_column(u'mapelements_mappoint', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


        # Changing field 'MapPoint.coordinates'
        db.alter_column(u'mapelements_mappoint', 'coordinates', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'MapPoint.address'
        db.delete_column(u'mapelements_mappoint', 'address')


        # Changing field 'MapPoint.coordinates'
        db.alter_column(u'mapelements_mappoint', 'coordinates', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        u'mapelements.mappoint': {
            'Meta': {'object_name': 'MapPoint'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type_of_point': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '255'})
        }
    }

    complete_apps = ['mapelements']