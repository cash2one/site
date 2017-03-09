# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'addressprogram_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('is_primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'addressprogram', ['Image'])

        # Adding model 'Construction'
        db.create_table(u'addressprogram_construction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 12, 22, 0, 0))),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'addressprogram', ['Construction'])

        # Adding model 'AdvertisingSpace'
        db.create_table(u'addressprogram_advertisingspace', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 12, 22, 0, 0))),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressprogram.GeoObject'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressprogram.Construction'])),
            ('side', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('backlight', self.gf('django.db.models.fields.CharField')(default='yes', max_length=5)),
            ('gid', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('grp', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ots', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('material', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('scheme', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'addressprogram', ['AdvertisingSpace'])

        # Adding field 'City.order'
        db.add_column(u'addressprogram_city', 'order',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'addressprogram_image')

        # Deleting model 'Construction'
        db.delete_table(u'addressprogram_construction')

        # Deleting model 'AdvertisingSpace'
        db.delete_table(u'addressprogram_advertisingspace')

        # Deleting field 'City.order'
        db.delete_column(u'addressprogram_city', 'order')


    models = {
        u'addressprogram.advertisingspace': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'AdvertisingSpace'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.GeoObject']"}),
            'backlight': ('django.db.models.fields.CharField', [], {'default': "'yes'", 'max_length': '5'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 22, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'grp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ots': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'scheme': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'side': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Construction']"})
        },
        u'addressprogram.city': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'City'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'based': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 22, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'emblem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'population': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Region']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'addressprogram.construction': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Construction'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'addressprogram.geoobject': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'GeoObject'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.City']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 22, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'addressprogram.image': {
            'Meta': {'object_name': 'Image'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'addressprogram.region': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Region'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 22, 0, 0)'}),
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