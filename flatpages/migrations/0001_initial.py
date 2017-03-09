# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FlatPage'
        db.create_table(u'flatpages_flatpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='child', null=True, to=orm['flatpages.FlatPage'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('menu_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='text', max_length=255)),
            ('show_in_menu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('show_in_side_menu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal(u'flatpages', ['FlatPage'])

        # Adding model 'IndexPage'
        db.create_table(u'flatpages_indexpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'flatpages', ['IndexPage'])

        # Adding model 'Advantage'
        db.create_table(u'flatpages_advantage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('show', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'flatpages', ['Advantage'])

        # Adding model 'Manager'
        db.create_table(u'flatpages_manager', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('man_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('sub_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('order', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('show', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'flatpages', ['Manager'])


    def backwards(self, orm):
        # Deleting model 'FlatPage'
        db.delete_table(u'flatpages_flatpage')

        # Deleting model 'IndexPage'
        db.delete_table(u'flatpages_indexpage')

        # Deleting model 'Advantage'
        db.delete_table(u'flatpages_advantage')

        # Deleting model 'Manager'
        db.delete_table(u'flatpages_manager')


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
            'menu_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': u"orm['flatpages.FlatPage']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'show_in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_in_side_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'text'", 'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'})
        },
        u'flatpages.indexpage': {
            'Meta': {'object_name': 'IndexPage'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'flatpages.manager': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Manager'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'man_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sub_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'})
        }
    }

    complete_apps = ['flatpages']