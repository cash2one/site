# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MapPoint.image'
        db.add_column(u'mapelements_mappoint', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MapPoint.image'
        db.delete_column(u'mapelements_mappoint', 'image')


    models = {
        u'mapelements.mappoint': {
            'Meta': {'object_name': 'MapPoint'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type_of_point': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '255'})
        }
    }

    complete_apps = ['mapelements']