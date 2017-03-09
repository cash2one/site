# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Construction.icon_hover'
        db.add_column(u'addressprogram_construction', 'icon_hover',
                      self.gf('django.db.models.fields.files.ImageField')(default='/media/images/logo.png', max_length=100),
                      keep_default=False)

        # Adding field 'Construction.icon_active'
        db.add_column(u'addressprogram_construction', 'icon_active',
                      self.gf('django.db.models.fields.files.ImageField')(default='/media/images/logo.png', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Construction.icon_hover'
        db.delete_column(u'addressprogram_construction', 'icon_hover')

        # Deleting field 'Construction.icon_active'
        db.delete_column(u'addressprogram_construction', 'icon_active')


    models = {
        u'addressprogram.advertisingspace': {
            'Meta': {'ordering': "('address__address', 'side')", 'object_name': 'AdvertisingSpace'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.GeoObject']"}),
            'backlight': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '5'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 3, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'material': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ots': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'scheme': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Construction']"})
        },
        u'addressprogram.city': {
            'Meta': {'ordering': "('order',)", 'object_name': 'City'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'available_constructions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['addressprogram.Construction']", 'symmetrical': 'False', 'blank': 'True'}),
            'based': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 3, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'emblem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'population': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Region']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'addressprogram.construction': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Construction'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 3, 0, 0)'}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/logo.png'", 'max_length': '100'}),
            'icon_active': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/logo.png'", 'max_length': '100'}),
            'icon_hover': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/logo.png'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker_icon': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/type1.png'", 'max_length': '100'}),
            'marker_icon_active': ('django.db.models.fields.files.ImageField', [], {'default': "'/media/images/type1-active.png'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'short_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_city': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'show_in_main': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'addressprogram.geoobject': {
            'Meta': {'ordering': "('address',)", 'object_name': 'GeoObject'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.City']"}),
            'construction': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'coordinates': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 3, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'prod': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['addressprogram.Construction']"})
        },
        u'addressprogram.image': {
            'Meta': {'object_name': 'Image'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'addressprogram.region': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Region'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2017, 2, 3, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['addressprogram']