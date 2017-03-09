# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GeoObject'
        db.create_table(u'addressprogram_geoobject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 12, 16, 0, 0))),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressprogram.City'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('is_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'addressprogram', ['GeoObject'])


        # Changing field 'City.name'
        db.alter_column(u'addressprogram_city', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'City.slug'
        db.alter_column(u'addressprogram_city', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Changing field 'City.based'
        db.alter_column(u'addressprogram_city', 'based', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'City.population'
        db.alter_column(u'addressprogram_city', 'population', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Deleting model 'GeoObject'
        db.delete_table(u'addressprogram_geoobject')


        # Changing field 'City.name'
        db.alter_column(u'addressprogram_city', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'City.slug'
        db.alter_column(u'addressprogram_city', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=100))

        # Changing field 'City.based'
        db.alter_column(u'addressprogram_city', 'based', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'City.population'
        db.alter_column(u'addressprogram_city', 'population', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'addressprogram.city': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'City'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'based': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 16, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'emblem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'population': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Region']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'addressprogram.geoobject': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'GeoObject'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.City']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 16, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'addressprogram.region': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Region'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 16, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['addressprogram']