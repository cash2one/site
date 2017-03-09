# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'addressprogram_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 12, 15, 0, 0))),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, blank=True)),
            ('is_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'addressprogram', ['Region'])

        # Adding model 'City'
        db.create_table(u'addressprogram_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2016, 12, 15, 0, 0))),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('emblem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addressprogram.Region'])),
            ('population', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('transport', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('based', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'addressprogram', ['City'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'addressprogram_region')

        # Deleting model 'City'
        db.delete_table(u'addressprogram_city')


    models = {
        u'addressprogram.city': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'City'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'based': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 15, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'emblem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addressprogram.Region']"}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'transport': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'addressprogram.region': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'Region'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 12, 15, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['addressprogram']