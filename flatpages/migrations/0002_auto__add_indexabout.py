# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'IndexAbout'
        db.create_table(u'flatpages_indexabout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('left_content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('right_content', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'flatpages', ['IndexAbout'])

    def backwards(self, orm):
        # Deleting model 'IndexAbout'
        db.delete_table(u'flatpages_indexabout')

    models = {
        u'flatpages.advantage': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Advantage'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'menu_title': (
            'django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True',
                                                          'to': u"orm['flatpages.FlatPage']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_in_side_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '255'}),
            'url': (
            'django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        u'flatpages.indexabout': {
            'Meta': {'object_name': 'IndexAbout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'left_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'right_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'flatpages.indexpage': {
            'Meta': {'object_name': 'IndexPage'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'flatpages.manager': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Manager'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'full_name': (
            'django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'man_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'position': (
            'django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sub_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'})
        }
    }

    complete_apps = ['flatpages']
